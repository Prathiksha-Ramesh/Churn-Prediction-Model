# Churn Prediction Model

## Overview
This project focuses on predicting customer churn using a machine learning model. The model is built using various Python libraries and trained on the `Churn_Modelling.csv` dataset. It includes the necessary steps for data preprocessing, model training, and evaluation. The project provides a Streamlit app for easy interaction with the model.

## Table of Contents
- Project Structure
- Installation
- Usage
- Model Details
- Deployment on Streamlit Cloud
- License
- Contributing
- Acknowledgments

## Project Structure
The project is organized as follows:

├── app.py                      # Streamlit app for model interaction  
├── notebook.ipynb              # Jupyter notebook for exploratory data analysis and model development  
├── prediction.ipynb            # Jupyter notebook for model predictions  
├── model.h5                    # Saved trained model  
├── scaler.pkl                  # Scaler for preprocessing features  
├── label_encoder_gender.pkl    # Label encoder for gender feature  
├── ohe.pkl                     # One hot encoder for categorical features  
├── requirements.txt            # Python dependencies  
├── Churn_Modelling.csv         # Dataset used for model training  
├── LICENSE                     # Project's license file  
├── .gitignore                  # Git ignore file  

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**  
   `git clone https://github.com/yourusername/churn-prediction.git`  
   `cd churn-prediction`

2. **Create a virtual environment and activate it:**  
   `python -m venv venv`  
   `source venv/bin/activate`  *(On Windows use `venv\Scripts\activate`)*

3. **Install the required dependencies:**  
   `pip install -r requirements.txt`

## Usage

### Running the Streamlit App
You can run the Streamlit app to interact with the model:

`streamlit run app.py`

### Model Training and Evaluation
You can explore the model training and evaluation process using the Jupyter notebooks provided:

- **notebook.ipynb:** Contains exploratory data analysis and the model training process.
- **prediction.ipynb:** Contains the code for making predictions using the trained model.

## Model Details
The model is a deep learning neural network built using TensorFlow/Keras. It includes the following steps:

- **Data Preprocessing:** Scaling, encoding categorical variables, and handling missing values.
- **Model Architecture:** A neural network with multiple layers, designed to predict churn.
- **Evaluation:** The model is evaluated using various metrics like accuracy, precision, recall, and F1-score.

## Deployment on Streamlit Cloud
You can easily deploy this project to Streamlit Cloud by following these steps:

1. **Fork the repository** *(if you haven't already):*  
   Go to the GitHub repository and click on the "Fork" button to create a copy of the repository in your GitHub account.

2. **Deploy to Streamlit Cloud:**  
   Sign in to [Streamlit Cloud](https://streamlit.io/cloud) with your GitHub account.  
   Click on "New app" and choose the repository and branch you want to deploy.  
   Specify the `app.py` as the entry point for the app.  
   Click "Deploy."

3. **Environment Variables (if required):**  
   If your app requires any environment variables, you can set them in the Streamlit Cloud settings under the "Advanced Settings" tab.

4. **Access your deployed app:**  
   Once deployed, Streamlit will provide you with a URL where your app is live and accessible to others.

## License
This project is licensed under the Apache License - see the `LICENSE` file for details.

## Contributing
Contributions are welcome! Please submit a pull requests.

## Acknowledgments
This project was developed as part of a data science project. Special thanks to the udemy course instructor and the open-source community for the tools and libraries used in this project.
