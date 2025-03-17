# data-science-global-college

# Project Overview
This project analyzes global college statistics, focusing on student demographics, academic performance, faculty counts, and placement rates. It involves data preprocessing, exploratory analysis, visualization, and predictive modeling to gain insights from the dataset.

# Folder Structure
```
project-root/
├── data/               # Contains raw and cleaned datasets
├── scripts/            # Python scripts for data processing and analysis
├── outputs/            # Stores generated reports, visualizations, and model outputs
├── requirements.txt    # List of required dependencies
├── README.md           # Project documentation
```

# Usage
## 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:
```sh
pip install -r requirements.txt
```

## 2. Run the Scripts:
### Data Preprocessing
Clean and preprocess the dataset:
```sh
python scripts/01_data_preprocessing.py
```

### Exploratory Analysis
Generate summary statistics and correlation matrix:
```sh
python scripts/02_exploratory_analysis.py
```

### Data Visualization
Create key visualizations:
```sh
python scripts/03_visualizations.py
```

### Model Training
Train a regression model to predict placement rates:
```sh
python scripts/04_modeling.py
```

### Model Evaluation
Analyze model performance and generate insights:
```sh
python scripts/05_results_analysis.py
```

# Requirements
- Python 3.x
- pandas
- matplotlib
- scikit-learn
- joblib

# Acknowledgments
**Dataset Name:** Global College Statistics Dataset  
**Dataset Author:** Sameerk  
**Dataset Source:** [Global College Statistics Dataset](https://www.kaggle.com/datasets/sameerk2004/global-college-statistics-dataset)