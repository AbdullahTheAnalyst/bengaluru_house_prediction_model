```markdown
# 🏠 Bengaluru House Price Prediction

This project uses **Machine Learning** to predict house prices in **Bengaluru, India**. A **Linear Regression** model is trained and deployed using a user-friendly **Streamlit** web app.

## 📂 Project Structure

- `House_Prediction_Model_LinearRegression.pkl` — Pretrained regression model.
- `app.py` — Streamlit app for prediction.
- `Bengaluru_House_Data.csv` — Dataset used to train the model.
- `requirements.txt` — Required Python packages.

## 🚀 Features

- Takes user input:
  - Total square footage (`total_sqft`)
  - Number of bedrooms (`bhk`)
  - Number of bathrooms (`bath`)
  - Location (via one-hot encoding)
- Predicts the **house price** in **₹ Lakh**

## 🧠 ML Model

- Algorithm: `LinearRegression` (from scikit-learn)
- Categorical encoding: One-hot (for `location`)
- Cleaned dataset before training

## 📊 Dataset

- Source: Bengaluru real estate (open dataset)
- Key columns: `location`, `total_sqft`, `bath`, `bhk`, `price`

## ▶️ Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Launch Streamlit app
streamlit run app.py

![image](https://github.com/user-attachments/assets/32fa75c3-8e8b-48b7-990f-a5bbdba05b60)

