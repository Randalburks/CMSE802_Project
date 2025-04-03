# CMSE802_Project
# Customer Segmentation and Psychographic Profiling  
**By Randal Burks**  
*burksran@msu.edu*

## Overview  
This project enhances targeted marketing using **clustering** and **sentiment analysis** to group customers based on their behavior, preferences, and values. Traditional methods rely too much on age or gender — this approach goes deeper using actual reviews and behavior.

## Problem Statement  
Current segmentation methods, like rule-based grouping or basic K-means clustering, often miss nuanced insights. They don’t capture niche customer groups or emotional motivations.  
This project improves segmentation by combining:
- **K-means + DBSCAN** for flexible customer clustering  
- **NLP sentiment analysis** on review text to detect customer values and attitudes

Goal: Uncover deeper psychographic profiles and support more personalized marketing strategies.

## Dataset  
Using the **Women's Clothing E-Commerce Reviews** dataset (from Kaggle):  
- 23,486 customer reviews in CSV format  
- Includes both structured data and unstructured review text  
- Key columns:
  - `Clothing ID`, `Age`, `Rating`, `Recommended`, `Positive Feedback Count`, `Review Text`, `Division Name`, `Department Name`, `Class Name`

## 📁 Project Structure



/src/        - Source code modules and Python scripts (.py files)
/notebooks/  - Jupyter notebooks for analysis and visualization
/data/       - Raw and processed data files or data source documentation
/tests/      - Unit tests for validating implementation
/docs/       - Supplementary documentation or reports
/results/    - Model outputs, figures, and saved checkpoints
README.md    - Overview and instructions for the repository
requirements.txt - List of package dependencies

## Code Plan
- Implement clustering and sentiment analysis in `.py` files inside `/src/`
- Use notebooks in `/notebooks/` to visualize clusters and results
- Use the `/tests/` folder to write basic unit tests (e.g. for text cleaning or model predictions)
- Include docstrings and comments to make code clear
- Keep data handling, modeling, and visualization separated for clarity

---

This structure and setup supports modular development and makes it easier to test, analyze, and explain the results.
