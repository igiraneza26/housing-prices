import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_features_insights import page_correlation_insights_body
from app_pages.page_inherited_predictions import page_inherited_predictions_body
from app_pages.page_predict_price import page_predict_price_body
from app_pages.page_project_hypothesis import page_hypothesis_validation_body
from app_pages.page_technical_report import page_technical_report_body


app = MultiPage(app_name= "Heritage Housing Issues") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Features Insights", page_correlation_insights_body)
app.add_page("Inherited House Predictions", page_inherited_predictions_body)
app.add_page("Predict Your House Price", page_predict_price_body)
app.add_page ("Hypothesis Validation", page_hypothesis_validation_body)
app.add_page("Technical Report", page_technical_report_body)
app.run() # Run the  app
