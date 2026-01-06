# AI-Powered Payroll Anomaly Detection

## Problem Statement
In real-world payroll systems, anomalies such as salary manipulation or fake overtime can occur.
However, labeled fraud data is usually not available, which makes supervised learning difficult.

## Solution Overview
This project uses an unsupervised anomaly detection approach to learn normal payroll behavior
and automatically flag unusual salary and overtime patterns.

## Why Unsupervised Learning?
Payroll fraud labels are rare and unreliable.
Instead of training on labeled data, the model learns what normal payroll behavior looks like
and identifies deviations as potential anomalies.

## Feature Engineering 
Instead of using raw salary values, behavior-based features were created:
- **OvertimeRatio**: Overtime pay relative to base salary
- **OtherPayRatio**: Additional pay relative to base salary
- **BenefitsRatio**: Benefits relative to base salary
- **ExtraPayAmount**: Difference between total pay and base salary

These features help capture abnormal payroll behavior more effectively.

## Anomaly Detection Approach
Isolation Forest is used as the anomaly detection model.
It isolates unusual data points without requiring labeled examples,
making it suitable for fraud detection scenarios.

## Results
The model flags a small percentage of employees as potential anomalies.
These cases typically show unusually high overtime ratios or excessive extra pay.

## Deployment Strategy
- **Batch Processing**: Monthly payroll audits to detect long-term anomalies
- **Real-Time Processing**: Validation of new payroll entries before approval
- **Concept Drift Handling**: Periodic retraining using recent payroll data

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn

