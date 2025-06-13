import streamlit as st

def page_summary_body():
    st.write("### Quick Project Summary")

    # Overview: contextualizing this project
    st.info(
        f"**Project Context**\n"
        f"* This project focuses on the **Ames Housing dataset**, a public dataset of home sales in Ames, Iowa.\n"
        f"* The objective is to **analyze how house attributes influence sale prices**, and use that to build a predictive system.\n"
        f"* The client has **inherited 4 houses**, and is interested in estimating their market value as well as any future properties.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset contains detailed attributes for each house including structural features "
        f"(e.g., floor area, garage size, basement finish), quality ratings (e.g., kitchen, materials), and sale price.\n"
        f"* Variables include both numerical (like square footage) and categorical (like kitchen quality, basement exposure) features.")

    # Optional: link to README
    st.write(
        f"* For a deeper dive, see the "
        f"[full project documentation and README](https://github.com/your-repo-link)."
    )

    # Business requirements, adapted from your brief
    st.success(
        f"**The project meets 4 business requirements:**\n"
        f"* **1 - Correlation Discovery:** Identify which features most strongly correlate with sale price through visualizations.\n"
        f"* **2 - Price Prediction:** Predict sale prices for the 4 inherited homes and allow dynamic prediction for any new house.\n"
        f"* **3 - User Interface:** Deliver a user-friendly interactive dashboard (this one).\n"
        f"* **4 - Success Criteria:** Ensure R² ≥ 0.75, report top price drivers, and display the summed value of inherited homes."
    )