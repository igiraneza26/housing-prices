import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page_inherited_predictions_body():
    st.write("### Inherited Houses: Predicted Sale Prices")

    # Info box explaining the page
    st.info(
        f"**Page Purpose**\n"
        f"* The client inherited 4 properties in Ames, Iowa.\n"
        f"* Using the trained ML model, we predict the **expected sale price** of each property.\n"
        f"* These estimates help the client evaluate total resale value and plan financially.\n\n"
        f"**How It Works**\n"
        f"* The model uses structural and qualitative house attributes (e.g., square footage, quality ratings) "
        f"to generate a price estimate for each inherited house.\n"
        f"* All 4 houses were preprocessed using the same transformations applied to the training data."
    )

    # Load predicted data
    inherited_path = "outputs/predictions/inherited_house_predictions.csv"
    try:
        df_inherited = pd.read_csv(inherited_path)

        # Show table
        st.subheader("Predicted Sale Prices")
        st.dataframe(df_inherited[['Predicted_SalePrice']].rename(
            columns={'Predicted_SalePrice': 'Predicted Sale Price ($)'}))

        # Sum total value
        total_value = df_inherited['Predicted_SalePrice'].sum()
        st.success(f"💰 **Total Predicted Value of the 4 Inherited Houses:** ${total_value:,.0f}")

        # Optional: plot
        st.subheader("Predicted Prices by Property")
        fig, ax = plt.subplots()
        sns.barplot(data=df_inherited, y='Predicted_SalePrice', x=df_inherited.index + 1, ax=ax)
        ax.set_ylabel("Predicted Sale Price ($)")
        ax.set_xlabel("Inherited House #")
        ax.set_title("Estimated Market Value of Inherited Properties")
        st.pyplot(fig)

    except FileNotFoundError:
        st.warning("Predicted results for inherited houses not found. Please run the prediction step and save the results to `outputs/predictions/inherited_house_predictions.csv`.")