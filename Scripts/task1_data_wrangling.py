# ============================================================
# Task 1 : Data Immersion & Wrangling
# ApexPlanet Data Analytics Internship
# Author : Kottakota Gayatri
# ============================================================

# Import Required Libraries
import pandas as pd
import numpy as np
import os

# ============================================================
# File Paths
# ============================================================

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(
    base_path,
    "Dataset",
    "Raw",
    "ApexPlanet_DataAnalytics_Dataset.xlsx"
)

cleaned_path = os.path.join(
    base_path,
    "Dataset",
    "Cleaned",
    "Cleaned_ApexPlanet_DataAnalytics_Dataset.xlsx"
)

# ============================================================
# Load Dataset
# ============================================================

print("=" * 60)
print("TASK 1 : DATA IMMERSION & WRANGLING")
print("=" * 60)

print("\nLoading Dataset...\n")

df = pd.read_excel(dataset_path)

print("Dataset Loaded Successfully!")

# ============================================================
# Dataset Preview
# ============================================================

print("\n" + "=" * 60)
print("FIRST FIVE ROWS")
print("=" * 60)

print(df.head())

# ============================================================
# Dataset Shape
# ============================================================

print("\n" + "=" * 60)
print("DATASET SHAPE")
print("=" * 60)

print(df.shape)

# ============================================================
# Column Names
# ============================================================

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)

print(df.columns)

# ============================================================
# Dataset Information
# ============================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

df.info()

# ============================================================
# Missing Values
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

# ============================================================
# Duplicate Records
# ============================================================

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

print(df.duplicated().sum())

# ============================================================
# Numerical Summary
# ============================================================

print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)

print(df.describe())

# ============================================================
# Categorical Summary
# ============================================================

print("\n" + "=" * 60)
print("CATEGORICAL SUMMARY")
print("=" * 60)

print(df.describe(include="object"))

# ============================================================
# Data Types
# ============================================================

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)

# ============================================================
# Data Cleaning
# ============================================================

print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

# Convert Order_Date to DateTime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Fill missing Age values using Median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing City values using Mode
df["City"] = df["City"].fillna(df["City"].mode()[0])

# Convert Age into Integer
df["Age"] = df["Age"].astype(int)

print("Data Cleaning Completed Successfully!")

# ============================================================
# Feature Engineering
# ============================================================

print("\n" + "=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

# Extract Year
df["Year"] = df["Order_Date"].dt.year

# Extract Month
df["Month"] = df["Order_Date"].dt.month_name()

# Create Age Groups
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[17, 30, 45, 60, 100],
    labels=["Young", "Adult", "Middle Age", "Senior"]
)

print("Feature Engineering Completed!")

# ============================================================
# Updated Dataset Preview
# ============================================================

print("\n" + "=" * 60)
print("UPDATED DATASET")
print("=" * 60)

print(df.head())

# ============================================================
# Save Cleaned Dataset
# ============================================================

df.to_excel(cleaned_path, index=False)

print("\nCleaned Dataset Saved Successfully!")

# ============================================================
# Project Completed
# ============================================================

print("\n" + "=" * 60)
print("TASK 1 COMPLETED SUCCESSFULLY")
print("=" * 60)