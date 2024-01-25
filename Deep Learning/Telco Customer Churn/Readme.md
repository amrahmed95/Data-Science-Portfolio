# Telco Customer Churn #

## 1. Project Overview ##

The purpose of the Telco Customer Churn dataset is to analyze and predict customer churn for a telecommunications company. 
Customer churn, also known as customer attrition, refers to the phenomenon where customers discontinue their services or subscriptions with a company.
Understanding and predicting customer churn is critical for businesses, including telecommunications companies, as it directly impacts revenue, 
customer satisfaction, and market competitiveness. 
By analyzing customer behavior and identifying potential churners, companies can take proactive measures to retain customers, improve service quality, and enhance customer loyalty.

## 1. Background ##

In this project I will predict customer churn. In this project the following steps were excluded:

* Loading the data
* Exploring data
* Preprocessing the data
* Exploratory Data Analysis
* Feature Engineering
* Develop prediction model (Artificial neural network - ANN)
* Evaluate and visualize the results

## 2. Data Exploration and Preprocessing ##

Data Exploration section aims to provide insights into the dataset's structure, distribution, and relationships between variables.

* Distribution of monthly charges, Total Charges
* Distribution of contract types, Payment method with respect to the churn
* Distribution of churn with respect to the gender, tenure, charges

## 3. Feature Engineering ##

* Label Encoding
* Standard Scaling

## 4. Model Building and Training 

* Train the ANN model on the training data using appropriate optimization algorithm (Adam Optimizer) and loss function (Binary Cross Entropy).
* Use Keras Early stopping to stop wasting time.
 (early stopping is a form of regularization used to avoid overfitting when training a learner with an iterative method, such as gradient descent. 
  Such methods update the learner so as to make it better fit the training data with each iteration) -WikiPedia
* Evaluate the trained model on the test set to assess its performance using accuracy (~80%)

## 5. Dependencies

* Python 3.12.0
* pandas: Data manipulation and preprocessing.
* scikit-learn: Machine learning algorithms and model evaluation.
* tensorflow.keras: Deep learning framework for building neural network models.
* matplotlib and seaborn: Data visualization.

