import streamlit as st
import pandas as pd
import joblib
import json

def page_predict_price_body():
    st.write("### Predict Sale Price for Your Own House")

    st.info(
        f"**Page Purpose**\n"
        f"* This tool lets you estimate the market price of any house in Ames, Iowa based on its features.\n"
        f"* The prediction uses the same machine learning model and transformations applied during model training.\n\n"
        f"**How It Works**\n"
        f"* You fill in property details below (e.g., living area, quality ratings, lot size).\n"
        f"* The input is preprocessed and passed to the ML model to return an estimated sale price."
    )

    # Load model, encoder, feature order
    try:
        model = joblib.load("outputs/models/linear_regression_model.pkl")
        encoder = joblib.load("outputs/models/ordinal_encoder.pkl")
        with open("outputs/models/feature_order.json", "r") as f:
            feature_order = json.load(f)
    except:
        st.error("❌ Required model files not found. Please make sure model, encoder, and feature list are saved.")
        return

    # User input form
    with st.form("user_input_form"):
        st.write("Enter property details:")

        # Layout in columns
        col1, col2 = st.columns(2)

        with col1:
            GrLivArea = st.number_input("Above Grade Living Area (sq ft)", value=1500)
            GarageArea = st.number_input("Garage Area (sq ft)", value=400)
            TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", value=1000)
            BsmtExposure = st.selectbox("Basement Exposure", options=['Gd', 'Av', 'Mn', 'No', 'None'])

        with col2:
            LotArea = st.number_input("Lot Area (sq ft)", value=8000)
            KitchenQual = st.selectbox("Kitchen Quality", options=['Ex', 'Gd', 'TA', 'Fa', 'Po'])
            BsmtFinType1 = st.selectbox("Basement Finish Type", options=['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', 'None'])
            GarageFinish = st.selectbox("Garage Finish", options=['Fin', 'RFn', 'Unf', 'None'])

        submitted = st.form_submit_button("Predict Sale Price")

    if submitted:
        # Combine inputs into dictionary
        user_input = {
            'GrLivArea': GrLivArea,
            'GarageArea': GarageArea,
            'TotalBsmtSF': TotalBsmtSF,
            '1stFlrSF': 1200,
            'LotArea': LotArea,
            '2ndFlrSF': 300,
            'BedroomAbvGr': 3,
            'BsmtFinSF1': 600,
            'BsmtUnfSF': 400,
            'GarageYrBlt': 2005,
            'LotFrontage': 60,
            'MasVnrArea': 100,
            'OpenPorchSF': 40,
            'OverallCond': 5,
            'OverallQual': 6,
            'YearBuilt': 1995,
            'YearRemodAdd': 2005,
            'BsmtExposure': BsmtExposure,
            'BsmtFinType1': BsmtFinType1,
            'GarageFinish': GarageFinish,
            'KitchenQual': KitchenQual
        }

        # Build input DataFrame
        input_df = pd.DataFrame([user_input])

        # Handle missing categorical values (just in case)
        for col in ['BsmtExposure', 'BsmtFinType1', 'GarageFinish', 'KitchenQual']:
            input_df[col] = input_df[col].fillna('None')

        # Encode categoricals
        input_cat = input_df[['BsmtExposure', 'BsmtFinType1', 'GarageFinish', 'KitchenQual']]
        input_cat_encoded = encoder.transform(input_cat)

        # Combine numeric and encoded categorical
        input_num = input_df.drop(columns=['BsmtExposure', 'BsmtFinType1', 'GarageFinish', 'KitchenQual'])
        input_final = pd.concat([input_num.reset_index(drop=True), input_cat_encoded.reset_index(drop=True)], axis=1)

        # Reorder columns
        input_final = input_final[feature_order]

        # Predict
        predicted_price = model.predict(input_final)[0]

        st.success(f"**Estimated Sale Price: ${predicted_price:,.0f}**")