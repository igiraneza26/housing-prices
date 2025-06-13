# Housing Prices Predictive Analysis

## Dataset Content

This project uses the Housing Prices Dataset, a publicly available dataset containing detailed records on residential homes.

**Data Source:** [Housing Prices Dataset (Kaggle)](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)

**Selected Features in the Dataset:**

| Feature | Description | Range / Values |
|--------|-------------|----------------|
| 1stFlrSF | First Floor square feet | 334 – 4692 |
| 2ndFlrSF | Second Floor square feet | 0 – 2065 |
| BedroomAbvGr | Bedrooms above ground level | 0 – 8 |
| BsmtExposure | Basement exposure level | Gd, Av, Mn, No, None |
| BsmtFinType1 | Type of basement finish | GLQ, ALQ, BLQ, Rec, LwQ, Unf, None |
| BsmtFinSF1 | Finished basement area (type 1) | 0 – 5644 |
| BsmtUnfSF | Unfinished basement area | 0 – 2336 |
| TotalBsmtSF | Total basement area | 0 – 6110 |
| GarageArea | Garage size in square feet | 0 – 1418 |
| GarageFinish | Garage interior finish | Fin, RFn, Unf, None |
| GarageYrBlt | Garage year built | 1900 – 2010 |
| GrLivArea | Above ground living area | 334 – 5642 |
| KitchenQual | Kitchen quality | Ex, Gd, TA, Fa, Po |
| LotArea | Lot size in square feet | 1300 – 215245 |
| LotFrontage | Street frontage (linear feet) | 21 – 313 |
| MasVnrArea | Masonry veneer area | 0 – 1600 |
| EnclosedPorch | Enclosed porch area | 0 – 286 |
| OpenPorchSF | Open porch area | 0 – 547 |
| OverallCond | Overall condition (1 = worst, 10 = best) | 1 – 10 |
| OverallQual | Overall quality (1 = worst, 10 = best) | 1 – 10 |
| WoodDeckSF | Wood deck area | 0 – 736 |
| YearBuilt | Year built | 1872 – 2010 |
| YearRemodAdd | Remodel year | 1950 – 2010 |
| SalePrice | House sale price | 34,900 – 755,000 |

**Target Variable:**  
`SalePrice`: the final price of each home sale.

---

## Project Template Repository

This project is built on a standardized template for machine learning lifecycle management and dashboard deployment.

**Template Repo:** https://github.com/igiraneza26/housing-prices.git

This template includes:
- Folder scaffolding for data, notebooks, models, and deployment
- ML pipeline integration
- Streamlit-compatible dashboard components

---

## Business Requirements

1. **Correlation Discovery**  
   Identify which house attributes are most strongly correlated with sale price using visualizations.

2. **Price Prediction**  
   Build a model to:
   - Predict prices for 4 inherited houses.
   - Predict prices for any house using user inputs.

3. **User Interface**  
   Deliver an interactive dashboard (not an API).

4. **Success Criteria**  
   - Report on key sale price drivers
   - ML model achieving R² ≥ 0.75 on train and test sets
   - Sale price predictions for inherited houses
   - Input-enabled price estimator in dashboard

---

## Hypothesis & Validation Strategy

**Hypothesis 1:**  
Certain features like living area, garage size, and neighborhood are strongly correlated with sale price.

**Validation:**  
- Pearson Correlation and Predictive Power Score (PPS)
- Feature-target scatter plots

**Hypothesis 2:**  
A regression model trained on Housing Prices data can generalize to new houses in the city.

**Validation:**  
- Train-test split
- Cross-validation  
- R², MAE, RMSE evaluation

---

## Mapping Business Case to ML and Visualization Tasks

| Business Need | Visualization/ML Task |
|---------------|------------------------|
| Identify top price drivers | Correlation heatmaps, PPS plots, scatter plots |
| Predict prices | Regression modeling with Random Forest, XGBoost, etc. |
| User input prediction | Streamlit dashboard with form widgets |
| Communicate insights | Dashboard pages summarizing findings |

---

## ML Business Case Breakdown

| Model | Objective | Outcome | Metrics | Output | Heuristic | Training Data |
|-------|-----------|---------|---------|--------|-----------|----------------|
| Linear Regression | Baseline | Simple relationships | R², MAE | Predicted Price | Interpretability | Cleaned Housing Prices dataset |
| Random Forest | Robust non-linear modeling | Improved accuracy | R² ≥ 0.75 | Predicted Price | Feature importance | Same |
| XGBoost | Performance focus | High accuracy | Cross-validated R² | Predicted Price | Boosted trees | Same |
| (Optional) Neural Net | Experimental | Deep model performance | R², MAE | Predicted Price | Complex patterns | Scaled data |

---

## Dashboard Design (Streamlit)

| Page | Description |
|------|-------------|
| Project Summary | Overview, dataset description, client needs |
| Feature Insights | Correlation matrix, PPS heatmap, scatter plots |
| Predictions | Inputs for 4 houses, display individual and total predicted prices, user input form |
| Hypothesis Validation | Show tested hypotheses, validation steps |
| Technical Report | R², MAE, RMSE, model pipeline, feature importances |

---

## Summary

This project delivers a data-driven, interactive tool that identifies key drivers of home sale prices and enables the client to predict prices for inherited properties and any future real estate transactions.
