# Customer Purchase Prediction App

## Project Overview

The Customer Purchase Prediction App is a machine learning web application that predicts customer purchase behavior using customer data. It uses Python, Flask, and Scikit-learn to process customer information and generate predictions through a simple web interface.

Understanding customer purchase behavior helps businesses make better marketing decisions and improve customer engagement. This project uses a trained machine learning model to predict customer purchase outcomes based on relevant input features.

## Features

* **Purchase Prediction:** Predicts whether a customer is likely to make a purchase.
* **Machine Learning Model:** Uses a trained classification model to generate predictions.
* **Data Preprocessing:** Processes customer data before passing it to the model.
* **Web Interface:** Provides a user-friendly interface built with Flask.
* **Model Integration:** Loads the saved model and preprocessing encoders for prediction.
* **Deployment:** Supports deployment as a web application.

## Technologies Used

* **Programming Language:** Python
* **Web Framework:** Flask
* **Machine Learning:** Scikit-learn
* **Data Processing:** Pandas, NumPy
* **Model Storage:** Pickle
* **Frontend:** HTML, CSS
* **Deployment:** Render

## How It Works

1. **Input:** The user enters the required customer details through the web interface.
2. **Preprocessing:** The application prepares the input data using the appropriate preprocessing steps and encoders.
3. **Prediction:** The trained machine learning model analyzes the processed input.
4. **Result:** The application displays the predicted customer purchase outcome.

## Getting Started

### Prerequisites

* Python 3.10 or a compatible version supported by the project's dependencies.
* Git
* A code editor such as Visual Studio Code.

### Step 1: Clone the Repository

```bash
git clone https://github.com/harika047/customer-purchase-prediction-app.git
cd customer-purchase-prediction-app
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

Ensure that the trained model file and required preprocessing files are available in the expected locations before running the application.

## Live Demo

Access the deployed application:

[Customer Purchase Prediction App](https://customer-purchase-prediction-app.onrender.com)

## Applications

* Understanding customer purchase behavior.
* Supporting data-driven marketing decisions.
* Identifying potential customers.
* Improving customer engagement strategies.
* Applying machine learning to e-commerce problems.

## Future Improvements

* Compare multiple machine learning algorithms.
* Improve model performance through hyperparameter tuning.
* Display prediction probabilities.
* Enhance the user interface and data visualizations.
* Incorporate additional customer behavior features.

## Conclusion

The Customer Purchase Prediction App demonstrates the practical application of machine learning in understanding customer purchasing behavior. By integrating a trained machine learning model with a Flask web application, the project provides an accessible way to predict customer purchase outcomes based on input data. This project helped us gain practical experience in machine learning, data preprocessing, model integration, and web application development. It also highlights how data-driven predictions can support better business decisions and customer engagement.

