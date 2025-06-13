import streamlit as st

def page_hypothesis_validation_body():
    st.write("### Hypothesis Validation")

    st.info(
        f"**Purpose of This Page**\n"
        f"* Communicate the assumptions (hypotheses) we had before analyzing the data.\n"
        f"* Show how we validated each hypothesis using data analysis and visualizations.\n"
        f"* This helps the client understand how the analysis was grounded in business logic and evidence."
    )

    st.subheader("Tested Hypotheses")

    st.markdown("#### 1. Houses with larger above-ground living area (`GrLivArea`) sell for more")
    st.write(
        "* **Validated**: Strong positive correlation of ~0.71 with `SalePrice`.\n"
        "* Evident from scatter plot: more area → higher prices.\n"
        "* Included as a top feature in modeling."
    )

    st.markdown("#### 2. Better material quality (`OverallQual`) leads to higher prices")
    st.write(
        "* **Validated**: Highest correlation with `SalePrice` (~0.79).\n"
        "* Clear upward trend in scatter plot and supported by domain logic.\n"
        "* Key variable in predictive model."
    )

    st.markdown("#### 3. Houses with finished basements (`BsmtFinType1`, `BsmtExposure`) are more valuable")
    st.write(
        "* **Partially Validated**:\n"
        "* Encoded categories like 'GLQ' and 'Gd' showed higher median prices.\n"
        "* These categorical features were encoded and retained in the model."
    )

    st.markdown("#### 4. Garage size and quality matter")
    st.write(
        "* **Validated**:\n"
        "* `GarageArea` shows strong positive correlation (~0.62).\n"
        "* `GarageFinish` also included in the final model after encoding."
    )

    st.markdown("#### 5. Number of bedrooms (`BedroomAbvGr`) is a strong driver of price")
    st.write(
        "* **Rejected**:\n"
        "* Weak correlation (~0.16) with `SalePrice`.\n"
        "* Often adds space without increasing quality — excluded from top predictors."
    )

    st.markdown("#### 6. Recent construction (`YearBuilt`) or remodel (`YearRemodAdd`) increases value")
    st.write(
        "* **Supported**:\n"
        "* `YearBuilt` has a moderate correlation (~0.52).\n"
        "* Recent houses/remodels tend to fetch higher prices."
    )

    st.success(" All hypotheses were either validated or rejected based on exploratory data analysis and correlation tests.")
