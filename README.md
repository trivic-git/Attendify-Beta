


# Attendify-Beta

## Overview

Attendify is an innovative attendance application designed to streamline the process of taking attendance in university classes. By leveraging state-of-the-art face recognition technology, Attendify-Beta automates the tedious task of manual attendance, saving time and reducing errors.

![Example Image](assets\Attendify_v1.png)


## Features

- **Automated Attendance**: Automatically mark attendance by uploading photos of the class.
- **Face Recognition**: Uses DeepFace with RetinaFace detector and FaceNet model for accurate face recognition.
- **Attendance Report**: Generates attendance reports in CSV format.


## Tech Stack

- **Python**: Core programming language.
- **Streamlit**: Web framework for building the app interface.
- **DeepFace**: Library for face recognition.
- **OpenCV**: Library for image processing.
- **Pandas**: Library for data manipulation.
- **Pillow**: Library for image handling.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/Attendify-Beta.git
   cd Attendify-Beta
   ```

2. Install the required packages:

   ```sh
   pip install streamlit deepface opencv-python-headless pandas pillow
   ```

## Usage

1. Run the Streamlit app:

   ```sh
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the path to the student images database.

4. Upload images of the class (JPEG, PNG).

5. View the attendance results and download the attendance report in CSV format.

## Code Explanation

### `app.py`

This is the main script that runs the Streamlit app.

- **Libraries**: Imports necessary libraries including Streamlit, OpenCV, DeepFace, Pandas, and Pillow.
- **Functions**:
  - `draw_boxes`: Draws bounding boxes around detected faces and labels them.
  - `process_images`: Processes uploaded images to detect and recognize faces, draws bounding boxes, and generates attendance data.
- **Streamlit UI**: Provides a user interface for uploading images, entering the database path, and viewing results.


## Future Goals

1. **Improve Accuracy**: Enhance the face recognition accuracy by experimenting with different models and techniques.
2. **Real-time Processing**: Implement real-time video processing to mark attendance during live classes.
3. **Scalability**: Optimize the application to handle larger classes and more extensive databases efficiently.
4. **User Management**: Add features for managing user roles, such as different permissions for teachers and administrators.
5. **Integration**: Integrate with university systems for seamless data exchange and reporting.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue on GitHub.

---

We hope Attendify-Beta makes attendance management easier and more efficient for your institution!
```

