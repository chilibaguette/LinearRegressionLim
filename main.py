import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:\\Users\mrhum\Documents\CS-ELEC 1\heart_failure_clinical_records_dataset.csv")

data.isnull().sum()

data.describe()

