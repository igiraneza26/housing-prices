# Housing Prices Predictive Analysis

## Project Overview

This project delivers a data-driven, interactive application to support real estate price estimation in Ames, Iowa.  
It helps identify the most influential features driving house prices and predict values for both inherited and user-defined properties.

The end product is a Streamlit dashboard for both business users and technical audiences.

---

## Dataset Content

**Source:** [Housing Prices Dataset (Kaggle)](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)

The dataset contains 79 explanatory variables describing residential homes in Ames, Iowa, including:

| Feature         | Description                             | Range / Values           |
|-----------------|-----------------------------------------|---------------------------|
| GrLivArea       | Above ground living area                | 334 – 5642 sq ft          |
| GarageArea      | Size of garage in sq ft                 | 0 – 1418                  |
| TotalBsmtSF     | Total basement area                     | 0 – 6110 sq ft            |
| OverallQual     | Overall material and finish quality     | 1 (Very Poor) – 10 (Excellent) |
| YearBuilt       | Original construction year              | 1872 – 2010               |
| LotArea         | Lot size                                | 1300 – 215245 sq ft       |
| KitchenQual     | Kitchen quality                         | Ex, Gd, TA, Fa, Po        |
| ...             | ...                                     | ...                       |

**Target Variable:**  
`SalePrice` — the final selling price of each home.

---

## Deployed Application

**Live Dashboard:**  
[Click here to try the app](https://your-streamlit-app-url)  
(Replace with your actual deployment link)

---

## Business Requirements

1. Correlation Discovery  
   Identify which house attributes are most strongly correlated with sale price using data visualizations.

2. Price Prediction  
   - Predict the summed sale price for 4 inherited houses.  
   - Predict house prices dynamically using user-defined inputs.

3. Interactive Dashboard  
   Provide a self-contained dashboard (no API needed) for exploring insights and predicting prices.

4. Success Criteria  
   - Show key drivers of `SalePrice`  
   - ML model with R² ≥ 0.75 on both train and test sets  
   - Display total predicted value of inherited houses  
   - Enable live user input and instant price prediction

---

## Model Performance

| Metric     | Train Set | Test Set |
|------------|-----------|----------|
| R²         | 0.795     | 0.827    |
| MAE        | 20,899    | 22,541   |
| RMSE       | 34,937    | 36,396   |

Model performance meets the success benchmark (R² ≥ 0.75).

---

## Hypotheses and Validation

| Hypothesis                                                    | Status           |
|---------------------------------------------------------------|------------------|
| GrLivArea, OverallQual, GarageArea strongly influence price   | Validated        |
| More bedrooms lead to higher price                            | Rejected         |
| Newer homes (YearBuilt) increase value                        | Supported        |
| Finished basements and garages increase price                 | Validated        |

Validation methods:
- Pearson correlation and scatter plots
- Categorical encoding and model testing

---

## Business Mapping to ML and Visualization Tasks

| Business Question                                | ML/Analysis Method                       |
|--------------------------------------------------|------------------------------------------|
| What drives house prices?                        | Correlation matrix, scatter plots        |
| Can we predict inherited home prices?            | Regression modeling                      |
| How can users predict future prices?             | User-input form with live predictions    |
| How do we validate assumptions?                  | EDA, hypothesis testing                  |

---

## Machine Learning Models Used

| Model            | Purpose                     | Outcome                       |
|------------------|-----------------------------|-------------------------------|
| Linear Regression| Baseline and production model | High accuracy, interpretable |
| Encoder          | Ordinal categorical handling | BsmtExposure, KitchenQual    |

---

## Feature Engineering Summary

- Winsorization for outlier treatment
- Log, Box-Cox, and power transformations
- Ordinal encoding for categorical variables
- Final cleaned dataset stored in `/outputs/datasets/cleaned/`

---

## Dashboard Design (Streamlit)

| Page                        | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Quick Project Summary       | Overview of dataset and business needs                                      |
| Feature Correlation Insights| Explore strongest correlations to sale price via charts                     |
| Inherited House Predictions | View predictions and total estimated price for 4 inherited houses           |
| Predict Your House Price    | Interactive form to estimate price for a user-defined property              |
| Hypothesis Validation       | Summary of tested hypotheses and their validation results                   |
| Technical Report            | Model performance, feature importance, pipeline breakdown                   |

---

## Project Structure

```bash
├── app.py
├── app_pages/
│   ├── page_summary.py
│   ├── page_features_insights.py
│   ├── page_inherited_predictions.py
│   ├── page_predict_price.py
│   ├── page_project_hypothesis.py
│   └── page_technical_report.py
├── outputs/
│   ├── datasets/
│   │   └── cleaned/
│   ├── models/
│   │   └── linear_regression_model.pkl
│   │   └── ordinal_encoder.pkl
│   │   └── feature_order.json
│   └── evaluation/
│       └── metrics.json
