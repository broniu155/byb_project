# T18 - Multiple Linear Regression

## Description
This task involves performing multiple linear regression analysis using Python. Multiple linear regression is a statistical technique that models the relationship between a dependent variable and two or more independent variables. This task uses various datasets to demonstrate the application of multiple linear regression in different scenarios.

## Table of Contents
- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
  - [Running `multiple_linear_regression.ipynb`](#running-multiple_linear_regressionipynb)
  - [Running `diabetes_regression.ipynb`](#running-diabetes_regressionipynb)
  - [Running `diabetes_regression_improved.py`](#running-diabetes_regression_improvedpy)
  - [Data Files](#data-files)
    - [Advertising.csv](#advertisingcsv)
    - [diabetes.csv](#diabetescsv)
    - [diabetes_dirty.csv](#diabetes_dirtycsv)
  - [Example Outputs](#example-outputs)
- [Credits](#credits)

## Installation
To run the code for this task, you'll need to have Python and Jupyter Notebook installed on your machine. Additionally, you will need to install the required libraries. You can download and install Python from the [official website](https://www.python.org/downloads/). To install Jupyter Notebook and the required libraries, you can use the following commands:
```sh
pip install notebook
pip install pandas numpy matplotlib seaborn scikit-learn
```

After installing Python and Jupyter Notebook, clone the repository to your local machine using the following command:

```sh
git clone https://github.com/yourusername/yourrepository.git
```

Navigate to the task directory:

```sh
cd yourrepository/T18-Multiple-Linear-Regression
```

## Usage

### Running multiple_linear_regression.ipynb
To run the multiple_linear_regression.ipynb notebook, use the following command in your terminal:

```sh
jupyter notebook "multiple_linear_regression.ipynb"
```
This will open the Jupyter Notebook interface in your web browser. You can then run the cells in the notebook to execute the code and perform multiple linear regression analysis.

### Running diabetes_regression.ipynb
To run the diabetes_regression.ipynb notebook, use the following command in your terminal:

```sh
jupyter notebook "diabetes_regression.ipynb"
```
This will open the Jupyter Notebook interface in your web browser. You can then run the cells in the notebook to execute the code and perform regression analysis on the diabetes dataset.

### Running diabetes_regression_improved.py

To run the diabetes_regression_improved.py script, use the following command in your terminal:
```sh
python diabetes_regression_improved.py
```
This will execute the Python script that performs regression analysis on the diabetes dataset using improved techniques.

### Data Files

#### Advertising.csv
The Advertising.csv file contains data related to advertising budgets and sales. Here is a snippet of the file:

```sh
TV,Radio,Newspaper,Sales
230.1,37.8,69.2,22.1
44.5,39.3,45.1,10.4
...
```

#### diabetes.csv
The diabetes.csv file contains cleaned diabetes data. Here is a snippet of the file:

```sh
Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
6,148,72,35,0,33.6,0.627,50,1
1,85,66,29,0,26.6,0.351,31,0
...
```

#### diabetes_dirty.csv
The diabetes_dirty.csv file contains raw diabetes data that may need cleaning. Here is a snippet of the file:

```sh
Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
6,148,72,35,0,33.6,0.627,50,1
1,85,66,29,0,26.6,0.351,31,0
...
```

## Example Outputs
Here are some example outputs you can expect from running these notebooks and scripts:

### multiple_linear_regression.ipynb:

    Scatter plots with regression lines
    Summary statistics
    Model performance metrics

### diabetes_regression.ipynb:

    Regression analysis results
    Visualizations of the relationships between variables
    Model performance metrics

### diabetes_regression_improved.py:

```sh
Random Forest Regressor - MSE: 2879.263097345132
Random Forest Regressor - R2 Score: 0.456682631395827
Gradient Boosting Regressor - MSE: 2980.284634829389
Gradient Boosting Regressor - R2 Score: 0.4395245177439143
Best parameters for Random Forest: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 300}
Best Random Forest Regressor - MSE: 2870.249659187232
Best Random Forest Regressor - R2 Score: 0.45820898167531245
```

## Credits
This code was written by Broniu155. If you have any questions or suggestions, feel free to contact me.


Replace `https://github.com/yourusername/yourrepository.git` and `yourrepository` with the actual repository URL and name. Also, update `path_to_screenshot.png` with the actual path to the screenshot images if you have any.

Feel free to copy and paste the above markdown content into your README file. Let me know if you need further assistance!

