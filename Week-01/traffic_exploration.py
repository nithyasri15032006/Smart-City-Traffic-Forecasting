# ============================================
# Project: Forecasting of Smart City Traffic Patterns
# Week 1: Dataset Exploration
# Author: Nithyasri Murugan
# ============================================

# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 55)
print("Smart City Traffic Pattern Forecasting")
print("Week 1 - Dataset Exploration")
print("=" * 55)

# Load Dataset
# Replace the filename with your actual dataset name
df = pd.read_csv("traffic.csv")

# Display First 5 Rows
print("\nFirst 5 Rows:")
print(df.head())

# Display Last 5 Rows
print("\nLast 5 Rows:")
print(df.tail())

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns)

# Dataset Information
print("\nDataset Information:")
df.info()

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Records
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Data Types
print("\nData Types:")
print(df.dtypes)

# -----------------------------------
# Basic Visualization
# -----------------------------------

# Plot traffic distribution if 'Vehicles' column exists
if "Vehicles" in df.columns:
    plt.figure(figsize=(10,5))
    df["Vehicles"].hist(bins=20)
    plt.title("Traffic Volume Distribution")
    plt.xlabel("Number of Vehicles")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Plot junction count if 'Junction' column exists
if "Junction" in df.columns:
    plt.figure(figsize=(8,5))
    df["Junction"].value_counts().plot(kind="bar")
    plt.title("Traffic Records by Junction")
    plt.xlabel("Junction")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

print("\nWeek 1 Dataset Exploration Completed Successfully!")
