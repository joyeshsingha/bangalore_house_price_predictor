# 🏠 Bangalore House Price Prediction

A Machine Learning web application that predicts house prices in Bangalore using a **Random Forest Regression model** and an interactive **Streamlit dashboard**.

Built as an end-to-end ML project covering data cleaning, feature engineering, model training, and deployment.

---

## 🚀 Live Features

✅ Data Cleaning Pipeline  
✅ Feature Engineering & Outlier Removal  
✅ Random Forest Regression Model  
✅ Interactive Streamlit Web App  
✅ Location Dropdown Prediction Interface  
✅ Modular Production-Style Project Structure

---

## 📸 Application Preview

![App Screenshot](assets/app_demo.png)

---

## 🧠 Machine Learning Workflow

1. Data preprocessing and cleaning
2. Feature engineering
3. One-hot encoding of locations
4. Outlier removal
5. Model training using Random Forest Regressor
6. Model serialization using Joblib
7. Deployment with Streamlit

---

## 🛠 Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Random Forest Regressor**
- **Streamlit**
- **Joblib**

---

## 📂 Project Structure
Bangalore-House-Price-Prediction/
├── 📁 data/             # Contains all datasets
│   ├── 🗂 raw/          # Original unprocessed datasets
│   └── 🗂 processed/    # Cleaned and preprocessed datasets ready for modeling
├── 📓 notebooks/        # Jupyter notebooks for exploration and analysis
│   └── eda.ipynb        # Exploratory Data Analysis and visualizations
├── 🏷 models/           # Trained machine learning models and scalers
│   ├── house_price_model.pkl  # Serialized Random Forest Regressor model
│   └── scaler.pkl       # StandardScaler used during preprocessing
├── 🛠 src/              # Core scripts for ML workflow
│   ├── data_preprocessing.py  # Functions for cleaning and transforming data
│   ├── feature_engineering.py # Feature creation and encoding
│   ├── model_training.py      # Training pipeline and model saving
│   └── utils.py               # Helper functions used across scripts
├── 🌐 streamlit_app/    # Streamlit dashboard for interactive predictions
│   └── app.py            # Main app file for running Streamlit
├── 🖼 assets/           # Images, icons, and other media
│   └── app_demo.png      # Screenshot of the deployed app
├── 📜 requirements.txt  # Python dependencies for the project
└── 📖 README.md          # Project documentation (you’re reading this!)