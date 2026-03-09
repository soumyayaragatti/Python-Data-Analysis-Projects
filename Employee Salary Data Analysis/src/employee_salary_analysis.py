import numpy as np 
import pandas as pd

# loading csv file
df=pd.read_csv("C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Employee-Salary-Analysis\\data\\emplyoee_salary_dataset.csv")
print(df.head())

# handling missing data
print("Missing values:")
print(df.isnull().sum())
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print("Final missing values:")
print(df.isnull().sum())

# calculating department wise average salary
dept_sal=df.groupby("Department")["Salary"].mean()
dept_sal.to_csv("C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Employee-Salary-Analysis\\data\\Average_salary_per_department.csv")
print("Average salary per department is saved as 'Average_salary_per_department.csv'")

# salary hike if experience > 5 years
df["Updated_Salary"]=np.where(df["Experience"]>5,1.1*df["Salary"],df["Salary"])
print(df)

# detecting salary anomalies(outliers)
mean_salary=df["Salary"].mean()
std_salary=df["Salary"].std()
lower_bound=max(0,mean_salary-2*std_salary)
upper_bound=mean_salary+2*std_salary
df["Salary_Anomaly"]=np.where(((df["Salary"]<lower_bound) | (df["Salary"]>upper_bound)),"Yes","No")

# exporting CSV file
df.to_csv("C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Employee-Salary-Analysis\\data\\cleanedEmployeeSalary.csv",index=False)
print("Data cleaned completed! saved as 'cleanedEmployeeSalary.csv'")
