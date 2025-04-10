# Real Estate Price Predictor

This app has been built using Streamlit and deployed with Streamlit Community Cloud.

🔗 **Visit the app here**: [https://realestatesolution-kkdmte6utzdmsfbwtdw3ze.streamlit.app/]  
🔐 **Password** (if needed): `streamlit`

---

## 📋 Description

This app predicts property prices based on features such as square footage, number of rooms, and property type using regression models.

---

## 📁 Dataset

The model is trained on a structured dataset with features such as:
- Square footage
- Number of bedrooms
- Number of bathrooms
- Property type (e.g., Apartment, Bungalow)
- Location

---

## ⚙️ Technologies Used

- **Streamlit** – For building the interactive web application  
- **Scikit-learn** – For model training and evaluation  
- **Pandas & NumPy** – For data preprocessing and manipulation  
- **Matplotlib & Seaborn** – For data visualization and exploration (optional)

---

## 🤖 Model Summary

Trained using Linear Regression and Decision Tree Regressor on a housing dataset. It includes feature selection and mean absolute error evaluation.

---

## 🚀 Future Enhancements

- Add support for additional datasets  
- Incorporate explainability tools like SHAP or LIME  
- Add charts to visualize user inputs and predictions

---

## 🧪 Local Installation

```bash
git clone https://github.com/zoezoe513/Real_Estate_Solution
cd real_estate_price_predictor
python -m venv env
source env/bin/activate  # On Windows use `env\\Scripts\\activate`
pip install -r requirements.txt
streamlit run app.py
```

---

Thanks for using **Real Estate Price Predictor**! 🙌  
Feel free to contribute or share your feedback.
