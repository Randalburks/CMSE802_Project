# CMSE802 Project
# Customer Segmentation and Psychographic Profiling  
**By Randal Burks**  
*burksran@msu.edu*


# Sentiment Classification and Topic Modeling of Women's Clothing Reviews Using TF-IDF, Logistic Regression, and LDA

This project uses natural language processing and unsupervised learning techniques to extract meaningful insights from customer reviews in a women’s clothing e-commerce dataset.


## Problem Statement

Customer reviews are a rich source of feedback for e-commerce platforms. However, manually analyzing thousands of text reviews is time-consuming and inconsistent. This project aims to automate sentiment classification and explore natural groupings and topics in review data using machine learning techniques. By understanding the tone and themes of customer feedback, businesses can make informed decisions to improve products, marketing, and customer satisfaction.


## Project Overview

This project analyzes a dataset of 23,486 customer reviews from a women's clothing e-commerce platform in CSV format. The work is divided into the following stages:

1. **Data Cleaning and Preprocessing**  
   - Removed missing or null review texts  
   - Created a new "Sentiment" column by mapping numerical ratings to `Positive`, `Neutral`, and `Negative` categories  

2. **Sentiment Classification**  
   - Applied logistic regression to classify review sentiment using TF-IDF vectorization  
   - Evaluated performance with accuracy and a classification report  

3. **Clustering and Topic Modeling**  
   - Used KMeans and PCA to explore customer groupings  
   - Applied Latent Dirichlet Allocation (LDA) to extract topics from the reviews  
   - Evaluated clustering with silhouette score and Davies-Bouldin index  

4. **Visualization**  
   - Plotted sentiment distributions and clusters  
   - Displayed topic keywords and review groupings based on content themes  

5. **Insights**  
   - Identified relationships between sentiment, review text, and customer experience  
   - Highlighted actionable feedback and key topics expressed by customers  

The analysis was conducted using Python and Jupyter Notebooks, leveraging libraries such as `scikit-learn`, `nltk`, `pandas`, `matplotlib`, and `seaborn`.


## Structure

- `/src/`: Source code modules and Python scripts (.py files)  
- `/notebook/`: Jupyter notebook for analysis and visualization  
- `/data/`: Raw and processed data files or data source documentation   
- `/docs/`: Supplementary documentation or reports  
- `/results/`: Model outputs, figures, and saved checkpoints  
- `README.md`: Overview and instructions for the repository


## How to Run

1. Clone this repo  
2. Run `pip install -r requirements.txt`  
3. Open and run `/notebooks/Sentiment Code.ipynb`


## Dataset

The dataset contains 23,486 customer reviews in CSV format.  
Source: [Kaggle Dataset](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews)
