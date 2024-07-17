import streamlit as st
import cv2
import numpy as np
import pandas as pd
from deepface import DeepFace
import os
from PIL import Image, ImageDraw

def draw_boxes(image, faces, recognized_names):
    try:
        img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img)
        for i, face in enumerate(faces):
            x, y, w, h = face['x'], face['y'], face['w'], face['h']
            draw.rectangle([(x, y), (x+w, y+h)], outline="green", width=2)
            if i < len(recognized_names):
                name = os.path.basename(recognized_names[i])
                draw.text((x, y-15), name, fill="green")
            else:
                draw.text((x, y-15), "Unknown", fill="red")
        return np.array(img)
    except Exception as e:
        st.error(f"Error drawing boxes: {str(e)}")
        return None

def process_images(uploaded_files, db_path):
    recognized_faces = []
    total_faces = 0
    unknown_faces = 0
    processed_images = []

    for file in uploaded_files:
        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        try:
            # Detect faces
            faces = DeepFace.extract_faces(img_path=image, detector_backend='retinaface', enforce_detection=False)
            total_faces += len(faces)
            
            # Perform face recognition
            results = DeepFace.find(img_path=image, db_path=db_path, model_name='Facenet', detector_backend='retinaface', enforce_detection=False)
            
            recognized = []
            if isinstance(results, list) and len(results) > 0 and 'identity' in results[0].columns:
                recognized = results[0]['identity'].tolist()
                recognized_faces.extend(recognized)
                unknown_faces += len(faces) - len(recognized)
            else:
                unknown_faces += len(faces)
            
            # Prepare face coordinates for draw_boxes function
            face_coords = [{'x': face['facial_area'][0], 'y': face['facial_area'][1], 'w': face['facial_area'][2] - face['facial_area'][0], 'h': face['facial_area'][3] - face['facial_area'][1]} for face in faces]

            # Draw boxes on the image
            processed_image = draw_boxes(image, face_coords, recognized)
            if processed_image is not None:
                processed_images.append(processed_image)
            
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
    
    return recognized_faces, total_faces, unknown_faces, processed_images

# Streamlit UI
st.title("Class Attendance App")
st.write("Upload images to mark attendance")

db_path = st.text_input("Enter the path to student images database:")

uploaded_files = st.file_uploader("Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files and db_path:
    if not os.path.exists(db_path):
        st.error("The specified database path does not exist. Please provide a valid path.")
    else:
        st.write(f"Processing {len(uploaded_files)} images...")
        recognized_faces, total_faces, unknown_faces, processed_images = process_images(uploaded_files, db_path)
        
        st.write(f"Total faces detected: {total_faces}")
        st.write(f"Recognized faces: {total_faces - unknown_faces}")
        st.write(f"Unknown faces: {unknown_faces}")
        
        if recognized_faces:
            st.write("Attendance Marked for:")
            recognized_names = [os.path.basename(face) for face in recognized_faces]
            st.write(recognized_names)
            
            df = pd.DataFrame(recognized_names, columns=["Student Name"])
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Attendance", data=csv, file_name="attendance.csv", mime="text/csv")
        else:
            st.write("No faces recognized")
        
        # Display processed images
        for img in processed_images:
            st.image(img, use_column_width=True)
else:
    st.warning("Please upload images and provide a valid database path.")
