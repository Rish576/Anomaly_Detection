# Project Outcomes

This file explains the thinking and planning behind the AI/ML payroll anomaly detection project. The goal of the task was to create an engine that can identify unusual payroll behavior such as salary manipulation and fake overtime, even when labeled fraud data is not available.

---

## 1. Algorithm Selection Rationale

For this task, the dataset did not contain any labels indicating which records were fraudulent. Because of that, supervised machine learning could not be applied. I selected the **Isolation Forest** algorithm, which is an unsupervised learning technique designed specifically for detecting anomalies in tabular numerical data.

The algorithm learns the general pattern of normal payroll payments and isolates records that deviate strongly from those patterns. It works efficiently on large datasets and also supports retraining with new data, which helps in handling concept drift over time.

---

## 2. Pseudocode

The main logic of the project can be summarized as follows:

1. Load payroll dataset from a CSV file.  
2. Convert important payroll columns into numerical format.  
3. Clean the data by removing or correcting missing and invalid values.  
4. Create additional features based on human reasoning (for example, overtime ratio relative to base pay).  
5. Train the Isolation Forest model on numerical features.  
6. Use the trained model to assign anomaly scores to all records.  
7. Flag records with high anomaly scores as potential payroll fraud.  
8. Save the flagged anomalies into a new CSV file for further review.

---

## 3. Evaluation Strategy (No Labels)

Since the data has no ground-truth labels, evaluation was done using practical business logic rather than accuracy metrics. The following methods were used:

- Analyzing the distribution of anomaly scores produced by the model.  
- Measuring the percentage of records flagged as anomalies.  
- Verifying whether the flagged cases make sense according to payroll rules.  
- Comparing anomalies detected from older data versus recent data.  
- Using manual inspection of top unusual records.

This approach ensures that the model output is meaningful and useful in real-world scenarios.

---

## 4. Design of Pipelines

### Batch Pipeline

A batch processing pipeline was designed for periodic audits:

- Collect payroll records at regular intervals (such as monthly or quarterly).  
- Run the anomaly detection engine on the accumulated data.  
- Retrain the model using the most recent payroll information.  
- Generate a report of unusual payment patterns for HR and Finance teams.

### Real-Time Pipeline

A real-time pipeline was planned for new entries:

- Whenever a new payroll record is created, preprocess it automatically.  
- Use the already trained model to compute its anomaly score.  
- Immediately flag the record if it appears strongly unusual.  
- Store the result in an anomaly monitoring system.

Both pipelines together satisfy the company requirement of handling real-time as well as batch data.

---

## 5. Deployment Plan

To deploy this project in a real organization, the following steps are planned:

- Containerize the Python script using Docker so it can run on any system.  
- Schedule the batch pipeline through a CI/CD tool or cron job.  
- Host the real-time API version using AWS / Google Cloud.  
- Store anomaly results in cloud databases for tracking.  
- Continuously monitor model performance and retrain when needed.

---

### Final Result

The project successfully executed on an online payroll dataset and detected multiple unusual records. These anomalies are stored in **detected_payroll_anomalies.csv**, which can be used by the company teams for manual investigation and fraud prevention.
