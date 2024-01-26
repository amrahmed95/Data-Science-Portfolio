# Online Retail II #

## Project Overview: Online Retail Clustering Analysis with Sales Prediction

The "Online Retail Clustering Analysis with Sales Prediction" project focuses on clustering analysis of transaction data from a UK-based online retail store specializing in unique all-occasion gift-ware. In addition to clustering analysis, the project utilizes the FB Prophet library to predict sales for the upcoming years, leveraging historical transactional data.

## Project Objective:

The primary objective is twofold: first, to perform clustering analysis on transaction data to identify meaningful customer segments, product categories, and purchasing patterns; second, to forecast sales for the next years using the FB Prophet library. By clustering customers and products based on buying behavior and preferences and predicting sales trends, the project aims to provide actionable insights for targeted marketing strategies, inventory management, and business planning.

## Dataset:

The project utilizes a real online retail transaction dataset of a UK-based online retail store containing over 1 million records of information on customer purchases, product descriptions, quantities ordered, transaction dates, and country of purchase. The dataset spans two years, from 01/12/2009 to 09/12/2011, and includes transactions for a variety of unique all-occasion gift-ware items.

## Exploratory Data Analysis (EDA):

* Data Summary: Initial exploration of the dataset provides insights into its size, structure, and feature distributions. Summary statistics and visualizations help identify trends, outliers, and potential patterns in transaction data.

* Customer Segmentation: Clustering techniques are applied to group customers based on their purchasing behavior, frequency, and monetary value of transactions.

* Product Analysis: Clustering is also performed on products to identify distinct categories, popular items, and associations between products frequently purchased together.

* Market Basket Analysis: Association rules and frequent itemset mining techniques are used to uncover patterns in customer purchasing behavior and identify common item combinations.

* Sales Prediction with FB Prophet:
    - The FB Prophet library is used to forecast sales for the upcoming years based on historical transactional data.
        Time series analysis techniques are applied to identify seasonality, trends, and patterns in sales data, enabling accurate forecasting of future sales.
    - The predicted sales trends provide valuable insights for business planning, budgeting, and resource allocation.

## Methodology:

The project employs Principle Component Analysis (PCA) and unsupervised learning techniques such as K-means clustering to cluster customers and products based on transactional data. In addition, time series forecasting techniques using FB Prophet are applied to predict future sales trends.

## Key Steps:

* Data Preprocessing: The dataset undergoes preprocessing steps including data cleaning, handling missing values, and encoding categorical variables to prepare it for clustering analysis and time series forecasting.

* Feature Engineering: Relevant features such as total spending per customer, purchase frequency, and product categories may be derived to enhance clustering analysis.

* Clustering Analysis: K-means clustering is applied to the preprocessed data to identify meaningful customer segments and product categories.

* Sales Prediction: Historical sales data is analyzed using FB Prophet to forecast future sales trends and patterns.
Interpretation and Evaluation: Clusters and sales predictions are interpreted and evaluated based on their coherence, distinctiveness, and relevance to business objectives.

## Future Improvements:

- Integration of additional data sources such as customer demographics, website interactions, and marketing campaigns to enhance clustering analysis and customer segmentation.
- Further refinement of sales prediction models using additional features and advanced time series forecasting techniques.    

## Dependencies:

* Python 3.12.0
* pandas: Data manipulation and preprocessing.
* scikit-learn: Machine learning algorithms and model evaluation.
* matplotlib and seaborn: Data visualization.

## **This project overview provides stakeholders with a comprehensive understanding of the project's objectives, methodologies, and potential impact, fostering collaboration and transparency within the retail analytics community. Additionally, the inclusion of the FB Prophet library for sales prediction enhances the project's capabilities in forecasting future sales trends and patterns, empowering businesses to make informed decisions and strategic planning**