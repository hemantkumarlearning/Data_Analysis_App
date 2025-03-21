# Data Analysis App

## Overview

This Data Analysis App allows users to upload a CSV file, which is then analyzed and visualized using various features. The app displays the dataset as a DataFrame and categorizes the columns into numerical and categorical types. Users can easily visualize the columns using interactive plots created with Plotly. Additionally, the app offers a comparison feature that allows users to explore how a target column compares to all other columns in the dataset.

## Features

- CSV File Upload: Users can upload any CSV file for analysis.
- Dataframe Visualization: The uploaded CSV file is displayed as a DataFrame.
- Numerical and Categorical Column Detection: The app automatically categorizes columns into numerical and categorical types.
- Interactive Plots with Plotly: Visualize the data using interactive charts, such as histograms, box plots, and bar plots.
- Comparison Feature: Users can select a target column and compare it against all other columns in the dataset using various plots.
  
## Technologies Used

- Python: Backend scripting and data manipulation.
- Pandas: Data handling and analysis.
- Plotly: Data visualization for interactive charts.
- Streamlit: Web framework for building the interactive app.
  
## Installation

#### 1. Clone this repository:
```
git clone https://github.com/hemantkumarlearning/Data_Analysis_App.git
cd Data_Analysis_App
```

#### 2. Create a virtual environment (optional but recommended):
```
python -m venv venv
`venv\Scripts\activate`
```

#### 3. Install the required dependencies:

```
pip install -r requirements.txt
```

#### 4. Run the application:

```
streamlit run app.py
```


## Usage

- Upload a CSV File: Click on the "Upload CSV" button to select a file from your local machine.
- View the DataFrame: After uploading, the app will display the dataset as a table.
- Numerical and Categorical Columns: The app will automatically detect numerical and categorical columns and display them separately.
- Target Column Comparison: Select a target column, and the app will display comparisons between the target column and other columns in the dataset.
