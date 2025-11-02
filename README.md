# AI Health Diagnostics Tool (Advanced)

This project is an AI-powered app that predicts common diseases (cold, flu, fever, allergy, malaria, typhoid, or no risk) based on user symptoms using machine learning.

## Features

- Uses Decision Tree machine learning for diagnosis
- Predicts multiple diseases with 10 symptoms
- Easy-to-use Streamlit web app frontend
- Simple advice provided for each diagnosis

## How to Run Locally

1. *Install Python (Version 3.x required).*
   - Download from https://python.org if needed.
   - During installation, tick "Add Python to PATH".

2. *Install required packages in Command Prompt:*
    
    pip install streamlit pandas scikit-learn
    
    Or, if pip doesn’t work, try:
    
    py -m pip install streamlit pandas scikit-learn
    

3. *Clone or download the project repository:*
    
    git clone https://github.com/YOUR_USERNAME/ai_health_diagnostics.git
    
    Or manually download the files and put them in a folder.

4. *Navigate into the project folder:*
    
    cd ai_health_diagnostics
    

5. *Run the app:*
    
    streamlit run app.py
    

6. *Enter your symptoms in the browser to get predictions and advice!*

## File Details

- app.py: Main Python code for the Streamlit app
- data.csv: Sample dataset for model training
- README.md: Project information and setup instructions

## Customization

- Expand data.csv to improve model accuracy or add more diseases and symptoms.
- Edit advice messages in app.py as needed.

## Author

Ayush Naru
