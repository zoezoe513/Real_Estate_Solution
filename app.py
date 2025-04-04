import streamlit as st
import pandas as pd
import numpy as np
from data_loader import load_data
from model import train_linear_regression
from evaluate import evaluate_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


# Load and prepare data
df = load_data('final.csv')
x = df.drop('price', axis=1)
y = df['price']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train model
model = train_linear_regression(x_train, y_train)

# Streamlit UI
st.title("🏡 Real Estate Price Predictor")
st.markdown("Fill out the property details below to get a predicted price.")

# Dynamic inputs based on the feature columns
user_input = {}
for col in x.columns:
    if "sqft" in col or "area" in col:
        user_input[col] = st.number_input(f"{col.replace('_', ' ').title()}", min_value=0)
    elif df[col].dropna().nunique() == 2:
        user_input[col] = st.radio(f"{col.replace('_', ' ').title()}", options=[0, 1])
    else:
        user_input[col] = st.number_input(f"{col.replace('_', ' ').title()}", value=0)

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    st.success(f"🏡 Predicted Price: ${prediction:,.2f}")


# Add a header
st.subheader("📈 Model Evaluation: Actual vs Predicted Prices (Test Set)")

# Make predictions on the test set
y_pred = model.predict(x_test)

# Create the plot
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, alpha=0.6)
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
ax.set_xlabel("Actual Price")
ax.set_ylabel("Predicted Price")
ax.set_title("Actual vs Predicted")

# Show the plot in Streamlit
st.pyplot(fig)

