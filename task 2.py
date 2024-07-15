# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset (assuming it's in CSV format)
df = pd.read_csv('titanic.csv')

# Display basic information about the dataset
print("First few rows of the dataset:")
print(df.head())

print("\nColumns in the dataset:")
print(df.columns)

print("\nSummary statistics of numerical columns:")
print(df.describe())

print("\nInformation about the dataset:")
print(df.info())

# Data Cleaning
# Check for missing values
print("\nNumber of missing values in each column:")
print(df.isnull().sum())

# Fill missing values
# For example, filling missing 'Age' values with the median age
median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)

# For 'Embarked', fill missing values with the most common value
most_common_embarked = df
