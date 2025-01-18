import google.generativeai as genai
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Page configuration
st.set_page_config(layout='wide')
st.title("Math Problem Solver using Streamlit and LLM (Google Gemini)")

# API Key input
api_key = st.sidebar.text_input("Enter your Google API Key:", type="password", help="Get your API key from Google AI Studio")

if not api_key:
    st.warning("Please enter your Google API Key in the sidebar to continue.")
    st.stop()

try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
except Exception as e:
    st.error("Invalid API key. Please check your key and try again.")
    st.stop()

st.write("""
This project allows you to upload an image of a math equation or draw it directly, and send it to the LLM Gemini to receive a solution.

How to use this app:
1. Enter your Google API key in the sidebar
2. Upload an image containing the math problem OR use the drawing canvas to draw your equation
3. (Optional) Provide a text description of the problem
4. Click the 'Solve' button to send the input to Gemini
""")

# Create two columns
col1, col2 = st.columns([2, 1])

# Input method selection
with col1:
    input_method = st.radio("Choose input method:", ["Upload Image", "Draw Equation"])
    
    if input_method == "Upload Image":
        uploaded_file = st.file_uploader("Choose an image of a math problem", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
    else:
        canvas_result = st_canvas(
            stroke_width=2,
            stroke_color="#000000",
            background_color="#ffffff",
            height=300,
            width=600,
            drawing_mode="freedraw",
            key="canvas",
            display_toolbar=True
        )
        
        if canvas_result.image_data is not None:
            image = Image.fromarray(canvas_result.image_data.astype('uint8'))
            if image.mode == 'RGBA':
                image = image.convert('RGB')

    problem_text = st.text_area("Describe your problem (optional):",
                               placeholder="E.g., Solve this quadratic equation")

    solve_button = st.button('Solve')
    if solve_button:
        if ((input_method == "Upload Image" and uploaded_file is not None) or 
            (input_method == "Draw Equation" and canvas_result.image_data is not None)):
            with st.spinner('Processing your request...'):
                try:
                    base_prompt = """
                    Please analyze the mathematical problem in this image and provide:
                    1. The LaTeX representation of the problem
                    2. A step-by-step solution
                    3. The final answer
                    """
                    prompt = f"{base_prompt}\nAdditional context: {problem_text}" if problem_text else base_prompt
                    
                    response = model.generate_content([prompt, image])
                    st.session_state['solution'] = response.text
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    st.error("Please try again or use a different image")
        else:
            st.warning("Please provide an image (either upload or draw) before solving.")

# Display the solution
with col2:
    st.title("Solution")
    if 'solution' in st.session_state:
        st.markdown(st.session_state['solution'])
    else:
        st.info("Solution will appear here after processing")