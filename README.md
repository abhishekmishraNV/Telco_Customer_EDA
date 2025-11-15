# Telco Customer Churn Data Preprocessing

**Project Type:** Data Preprocessing & Feature Engineering Pipeline  
**Dataset:** Telco Customer Churn Dataset  
**Tools:** Python, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Category Encoders  
**Sample Data:** Included as CSV files

This repository contains a complete workflow for preprocessing the Telco Customer Churn dataset.  
It includes scripts for cleaning, encoding, scaling, binning, and analyzing data—designed as a  
reusable pipeline for machine learning or academic/technical projects.

---

## Overview

This project provides modular preprocessing steps widely used in data science pipelines.  
The workflow includes:

- **Handling Missing Values** – Imputation and removal logic  
- **Encoding** – Label, One-Hot, Dummy, Hashing, and Target encoding methods  
- **Feature Scaling** – Standard Scaling and MinMax Scaling  
- **Feature Binning** – Discretization of continuous features  
- **Outlier Detection** – Identify and optionally correct outliers  
- **Categorical & Numerical Analysis** – Univariate and bivariate analysis  

All scripts are independent and produce intermediate CSV outputs for easy verification.

---

## File Structure

| File/Folder               | Description                                           |
|----------------------------|-------------------------------------------------------|
| Cat-Num_Analysis.py       | Performs categorical + numerical univariate/bivariate analysis |
| Feature_Binning.py        | Discretizes continuous variables                     |
| Feature_encoding.py       | Implements all major encoding techniques             |
| FeatureScaling.py         | Standard and MinMax scaling routines                 |
| Handling_Missing_Values.py| Impute or drop missing values                         |
| Outlierspy.py             | Outlier detection and handling                        |
| Telco_customer_churn.csv  | Raw dataset                                          |
| Label-Encoder.csv         | Output: Label-encoded features                        |
| One hot Encoded.csv       | Output: One-hot encoded features                      |
| Hashing.csv               | Output: Hashed feature data                            |
| TargetEncoded.csv         | Output: Target-encoded data                           |
| test.csv                  | Output after binning                                   |
| README.md                 | Documentation                                        |

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/abhishekmishraNV/Telco_Customer_EDA.git
cd Telco_Customer_EDA

bash
Copy code
pip install pandas numpy scikit-learn matplotlib seaborn category_encoders
How to Run the Scripts
Option 1: Direct Execution
Run any script individually using Python:

bash
Copy code
python Feature_encoding.py
python FeatureScaling.py
python Handling_Missing_Values.py
python Feature_Binning.py
python Cat-Num_Analysis.py
Outputs (CSV files, charts, etc.) will be saved in the same folder.

Option 2: Modify Parameters
Open each file and customize input/output paths or parameters according to your dataset or preprocessing needs.

Sample Data
The repository includes a sanitized sample version of the Telco Customer Churn dataset.
Intermediate CSV outputs are generated after each preprocessing step for easy verification.

Results
Encoded datasets for multiple encoding strategies

Scaled numerical feature outputs

Binning outputs for selected columns

Visualizations for categorical/numerical relationships

Cleaned and preprocessed CSV files ready for modeling

Contributing
Pull requests are welcome.
For major changes, open an issue first to discuss the proposal.
Please ensure tests or documentation updates are included.