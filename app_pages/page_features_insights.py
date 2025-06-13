import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def page_correlation_insights_body():
    st.write("### Feature Correlation Insights")

    # Load dataset
    df = pd.read_csv("outputs/datasets/cleaned/train_set.csv")

    # Calculate correlations
    saleprice_corr = df.corr(numeric_only=True)['SalePrice'].sort_values(ascending=False).drop('SalePrice')
    top_features_corr = saleprice_corr.head(10)

    st.write("### Feature Correlation Insights")

    # Overview of the goal
    st.info(
        f"**Goal of this Page**\n"
        f"* To explore how individual house features are correlated with the final **sale price**.\n"
        f"* This helps the client understand which variables are most influential in determining home values.\n"
        f"* Strong correlations justify their use in predictive modeling.\n\n"
        f"**How We Did It**\n"
        f"* We computed Pearson correlations between all numeric features and the `SalePrice`.\n"
        f"* We focused on the top 10 features with the strongest positive correlation."
    )

    # Display correlation series
    st.subheader("Top 10 Features Most Correlated with Sale Price")
    st.dataframe(top_features_corr)

    # Plot scatterplots
    st.subheader("Scatter Plots of Top Features vs Sale Price")
    for feature in top_features_corr.index:
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=feature, y="SalePrice", ax=ax)
        ax.set_title(f"{feature} vs SalePrice")
        st.pyplot(fig)

    # Optional: heatmap
    st.subheader("Correlation Heatmap (Top Features Only)")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df[top_features_corr.index.tolist() + ['SalePrice']].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

    # Summary
    st.success(
        f"**Key Insights:**\n"
        f"* Features like `OverallQual`, `GrLivArea`, `GarageArea`, and `TotalBsmtSF` show strong positive correlation with `SalePrice`.\n"
        f"* Variables such as `BedroomAbvGr` or `EnclosedPorch` had weak or negative correlation and were excluded.\n"
        f"* These high-correlation features will be key inputs in the machine learning model."
    )
