import streamlit as st
import joblib
import pandas as pd

# Title
st.title("House Price Prediction App with Linear Regression Model")

# Model va ustunlar ro'yxatini yuklash
model, model_columns = joblib.load("House_Prediction_Model_LinearRegression.pkl")

# Location ustunlarini ajratib olish
location_columns = [col for col in model_columns if col not in ["total_sqft", "bath", "bhk"]]

# Foydalanuvchidan ma'lumot olish
location = st.selectbox("Location", sorted(location_columns))
sqft = st.number_input("Total Square Footage", min_value=1)
bath = st.number_input("Number of Bathrooms", min_value=1)
bhk = st.number_input("Number of Bedrooms", min_value=1)

# Bo'sh dataframe: barcha model ustunlari bilan
input_df = pd.DataFrame(data=[[0]*len(model_columns)], columns=model_columns)

# Raqamli ustunlarni joylashtirish
input_df.at[0, "total_sqft"] = sqft
input_df.at[0, "bath"] = bath
input_df.at[0, "bhk"] = bhk

input_df = pd.DataFrame(columns=model_columns)
input_df.loc[0] = 0  # barcha ustunlarga 0

# model_columns ichida mavjud bo‘lgan ustunlar uchun qiymat kiriting
if "bath" in input_df.columns:
    input_df.at[0, "bath"] = bath
if "total_sqft" in input_df.columns:
    input_df.at[0, "total_sqft"] = sqft
if "bhk" in input_df.columns:
    input_df.at[0, "bhk"] = bhk
if location in input_df.columns:
    input_df.at[0, location] = 1

# Tanlangan location uchun qiymatni 1 qilish
if location in input_df.columns:
    input_df.at[0, location] = 1
else:
    st.warning("Tanlangan location modelda mavjud emas. Iltimos boshqa birini tanlang.")

# Narxni taxmin qilish
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted House Price: ₹ {prediction:.2f} Lakh")

