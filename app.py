import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Title of the app
st.title("Real-Time Image Capture or Upload")

# # Select mode: Capture Image from webcam or Upload
# mode = st.selectbox("Select mode:", ["Capture from Webcam", "Upload an Image"])

# # If the user selects "Capture from Webcam"
# if mode == "Capture from Webcam":
#     st.write("Press the 'Start Webcam' button to capture an image.")
    
#     # Create a button to start the webcam
#     start_webcam = st.button("Start Webcam")
    
#     if start_webcam:
#         # Access the webcam
#         cap = cv2.VideoCapture(0)
#         st.write("Webcam Started. Press 'Capture Image' to take a photo.")
        
#         captured_image = None

#         while True:
#             ret, frame = cap.read()
#             if ret:
#                  st.write("image.png", frame)
#             if not ret:
#                 st.write("Failed to capture image.")
#                 break
            
#             # Show the live frame in Streamlit
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             st.image(frame_rgb, channels="RGB")
            
#             # Create a button to capture the image
#             capture_button = st.button("Capture Image")
            
#             if capture_button:
#                 captured_image = frame
#                 break

#         # Release the webcam
#         cap.release()

#         # if captured_image is not None:
#         #     st.write("Captured Image:")
#         #     captured_image_rgb = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)
#         #     st.image(captured_image_rgb, channels="RGB")

# If the user selects "Upload an Image"
if mode == "Upload an Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Convert the file to an image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)
