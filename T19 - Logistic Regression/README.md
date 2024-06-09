# T19 - Logistic Regression

## Description
This task involves performing logistic regression analysis using Python. Logistic regression is a statistical method for analyzing datasets in which there are one or more independent variables that determine an outcome. The outcome is a binary or dichotomous variable. This task uses the Iris dataset to demonstrate the application of logistic regression.

## Table of Contents
- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
  - [Running `Logistic_Regression.ipynb`](#running-logistic_regressionipynb)
  - [Running `iris_logistic_regression.ipynb`](#running-iris_logistic_regressionipynb)
  - [Running `iris.py`](#running-irispy)
  - [Data Files](#data-files)
    - [Iris.csv](#iriscsv)
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
cd yourrepository/T19-Logistic-Regression
```

## Usage

### Running Logistic_Regression.ipynb
To run the Logistic_Regression.ipynb notebook, use the following command in your terminal:

```sh
jupyter notebook "Logistic_Regression.ipynb"
```

This will open the Jupyter Notebook interface in your web browser. You can then run the cells in the notebook to execute the code and perform logistic regression analysis.

### Running iris_logistic_regression.ipynb
To run the iris_logistic_regression.ipynb notebook, use the following command in your terminal:

```sh
jupyter notebook "iris_logistic_regression.ipynb"
```
This will open the Jupyter Notebook interface in your web browser. You can then run the cells in the notebook to execute the code and perform logistic regression analysis on the Iris dataset.

### Running iris.py
To run the iris.py script, use the following command in your terminal:

```sh
python iris.py
```
This will execute the Python script that performs logistic regression analysis on the Iris dataset.

### Data Files

#### Iris.csv
The Iris.csv file contains the Iris dataset. Here is a snippet of the file:

```sh
Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species
1,5.1,3.5,1.4,0.2,Iris-setosa
2,4.9,3.0,1.4,0.2,Iris-setosa
...
```

## Example Outputs
Here are some example outputs you can expect from running these notebooks and scripts:

### Logistic_Regression.ipynb and iris_logistic_regression.ipynb:

    Summary statistics
    Model performance metrics such as accuracy, precision, and recall
    Visualizations of the relationships between variables and the confusion matrix

### iris.py:

```sh
Accuracy: 1.00
Classification Report:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         6
           1       1.00      1.00      1.00         6

 accuracy                              1.00        12
 macro avg         1.00      1.00      1.00        12
weighted avg       1.00      1.00      1.00        12

Confusion Matrix:
[[6 0]
[0 6]]
Precision: 1.00
Recall: 1.00
```

## Credits
This code was written by Broniu155. If you have any questions or suggestions, feel free to contact me.

Replace https://github.com/yourusername/yourrepository.git and yourrepository with the actual repository URL and name. Also, update path_to_confusion_matrix_image.png and path_to_screenshot.png with the actual path to the images if you have any.

Feel free to copy and paste the above markdown content into your README file. Let me know if you need further assistance!








