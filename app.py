import streamlit as st
from PIL import Image

# Function to generate a simple summary based on the uploaded image
def generate_summary(image):
    return "This is a summary of the uploaded image. The system identifies general content but this is a placeholder for a more advanced image analysis."

# Simulated chatbot response for now
def chatbot_response(query, summary):
    if "what" in query.lower():
        return f"You asked: {query}. Based on the image, here is a summary: {summary}"
    else:
        return "The chatbot is here to help answer questions about the uploaded image."

# Streamlit app
def main():
    # Title of the app
    st.title("Image Upload with Summary and Chatbot")

    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Upload Image", "View Image and Chat"])

    if page == "Upload Image":
        st.header("Step 1: Upload an Image")

        # Image uploader
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Display uploaded image
            img = Image.open(uploaded_file)
            st.image(img, caption="Uploaded Image", use_column_width=True)

            # Confirm button to proceed to the next page
            if st.button("Confirm and Proceed"):
                # Save the uploaded image and its summary in session state
                st.session_state['uploaded_image'] = img
                st.session_state['summary'] = generate_summary(img)
                st.session_state['page'] = "View Image and Chat"
                st.experimental_rerun()

    elif page == "View Image and Chat":
        st.header("Step 2: View Image, Summary, and Chat")

        # Check if an image has been uploaded
        if 'uploaded_image' in st.session_state:
            col1, col2 = st.columns([2, 1])

            # Left side: Display image and summary
            with col1:
                st.image(st.session_state['uploaded_image'], caption="Uploaded Image", use_column_width=True)
                st.write("### Image Summary")
                st.write(st.session_state['summary'])

            # Right side: Chatbot interface
            with col2:
                st.write("### Chatbot")
                user_input = st.text_input("Ask something about the image")
                if st.button("Submit"):
                    if user_input:
                        response = chatbot_response(user_input, st.session_state['summary'])
                        st.write(response)
                    else:
                        st.write("Please enter a question to ask the chatbot.")
        else:
            st.write("Please upload an image first on the 'Upload Image' page.")

if __name__ == "__main__":
    # Ensure session state exists to hold the image and summary
    if 'uploaded_image' not in st.session_state:
        st.session_state['uploaded_image'] = None
        st.session_state['summary'] = None
        st.session_state['page'] = None
    
    main()
