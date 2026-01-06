import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
df = pd.read_csv("Salaries.csv")
print("Dataset Loaded Successfully")
print("Total Records:", df.shape[0])
print("Columns in Dataset:", df.columns.tolist())

salary_cols = ["BasePay", "OvertimePay", "TotalPay"]

for col in salary_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["BasePay", "OvertimePay", "TotalPay"])

print("Cleaned Dataset Shape:", df.shape)
df["OvertimeRatio"] = df["OvertimePay"] / (df["BasePay"] + 1)

df["ExtraPayAmount"] = df["TotalPay"] - df["BasePay"]

features = df[["BasePay", "OvertimeRatio", "ExtraPayAmount"]]

print("Feature Engineering Completed")
print(features.head())


model = IsolationForest(contamination=0.02, random_state=42)

df["Anomaly"] = model.fit_predict(features)

anomalies = df[df["Anomaly"] == -1]

print("Anomaly Detection Completed")
print("Number of Anomalies Detected:", anomalies.shape[0])

anomalies[["EmployeeName", "JobTitle", "BasePay", "OvertimePay", "TotalPay"]].to_csv(
    "detected_payroll_anomalies.csv", index=False
)

print("Results Saved to detected_payroll_anomalies.csv")
anomaly_percent = anomalies.shape[0] / df.shape[0]
print("Current Anomaly Percentage:", round(anomaly_percent * 100, 2), "%")
print("Engine Execution Finished Successfully")
