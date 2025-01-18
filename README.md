# Math-To-LaTeX
### By Bram Nutt and Long Truong

This application allows users to solve mathematical problems by either uploading images of math equations or drawing them directly in the application. The app uses Google's Gemini AI model to analyze the problems and provide detailed solutions.

Check out our [website](https://mathtolatex.streamlit.app/)!
## Features

- Image upload support for math problems
- Interactive drawing canvas for equation input
- Optional text description field for additional context
- Step-by-step solution display
- LaTeX representation of problems
- Clean and intuitive user interface

## Prerequisites

- Python 3.8 or higher
- Google API key (from Google AI Studio)

## Installation
1. Clone this repository

2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Go the the [website](https://mathtolatex.streamlit.app/).

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. Access the application through your web browser 

3. Enter your Google API key in the sidebar

4. Choose your input method:
   - Upload an image of a math problem
   - Draw the equation using the canvas

5. (Optional) Add a text description of the problem

6. Click the "Solve" button to get the solution

## Configuration

The application requires a Google API key to function. You can obtain one from the [Google AI Studio](https://makersuite.google.com/app/apikey).

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini](https://deepmind.google/technologies/gemini/)
- Uses [streamlit-drawable-canvas](https://github.com/andfanilo/streamlit-drawable-canvas) for the drawing interface