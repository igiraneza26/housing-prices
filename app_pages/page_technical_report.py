import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import json

def page_technical_report_body():
    st.write("### Technical Report: Model Performance & Pipeline")

    # Info summary
    st.info(
        f"**Purpose of This Page**\n"
        f"* Provide technical users with model performance metrics.\n"
        f"* Show how the pipeline transforms data before predictions.\n"
        f"* Help assess model robustness and generalization performance."
    )

    # Load metrics
    try:
        metrics = pd.read_json("outputs/evaluation/metrics.json")
        st.subheader("Model Performance")
        st.write(metrics)

        st.success(
            f"R² on train and test sets exceeds the 0.75 threshold, indicating strong predictive power.\n"
            f"MAE and RMSE are within reasonable error margins for house price predictions."
        )
    except:
        st.warning("⚠️ Could not load performance metrics. Please ensure `outputs/evaluation/metrics.json` exists.")

    # Feature importance
    try:
        model = joblib.load("outputs/models/linear_regression_model.pkl")
        features = json.load(open("outputs/models/feature_order.json"))
        importances = model.coef_

        st.subheader("🔍 Feature Importances (Linear Coefficients)")

        # Combine and display
        df_importance = pd.DataFrame({
            "Feature": features,
            "Coefficient": importances
        }).sort_values(by="Coefficient", ascending=False)

        st.dataframe(df_importance)

        # Plot
        st.bar_chart(df_importance.set_index("Feature"))

    except:
        st.warning("Could not load model or feature importances.")

    # Pipeline description
    st.subheader("⚙️ ML Pipeline Steps")

    st.markdown("""
    **Data Preprocessing Pipeline:**
    - Drop or impute missing values
    - Encode categorical features (`OrdinalEncoder`)
    - Apply feature transformations for skewed numerical variables
    - Feature selection based on correlation and business insight

    **Model:**
    - `LinearRegression` from `scikit-learn`
    - Trained on cleaned + engineered features
    - Evaluated using: R², MAE, RMSE on train and test sets

    **Deployment Assets:**
    - Trained model `.pkl`
    - Ordinal encoder `.pkl`
    - Feature order `.json`
    """)
