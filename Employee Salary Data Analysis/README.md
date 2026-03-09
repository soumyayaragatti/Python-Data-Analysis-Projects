# 📊 Employee Salary Analysis

## 📌 Project Overview
This project analyzes employee salary data using **Python, NumPy, and Pandas**.
The goal is to clean salary data, perform department-wise analysis, apply
experience-based salary hikes, and detect salary anomalies using statistics.

---

## 📂 Dataset Description
The dataset contains the following columns:
- Employee_ID – Unique employee identifier
- Department – Department name
- Salary – Employee salary (may contain missing values)
- Experience – Years of experience

Each row represents one employee.

---

## 🎯 Objectives
- Handle missing salary values using the mean
- Calculate average salary per department
- Apply a 10% salary hike for employees with more than 5 years of experience
- Detect salary anomalies using mean ± 2 × standard deviation
- Export cleaned and analyzed data

---

## 🛠 Technologies Used
- Python
- NumPy
- Pandas

---

## 📚 Concepts Applied
- Data cleaning using `fillna()`
- Group-wise aggregation using `groupby()`
- Conditional logic using `np.where()`
- Statistical analysis using `mean()` and `std()`
- CSV file export using `to_csv()`

---

## 📈 Output Files
- `Average_salary_per_department.csv`
- `cleanedEmployeeSalary.csv`

---

## 🏁 Conclusion
This project demonstrates a real-world HR analytics workflow and builds a
strong foundation for data analyst roles.