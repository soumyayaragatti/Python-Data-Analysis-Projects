import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load csv file 
df=pd.read_csv("C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Student-Performance-Analyzer\\data\\Student_performance_dataset.csv")
print(df.head())

# handling missing values
print("Missing values:")
print(df.isnull().sum())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"]=df["English"].fillna(df["English"].mean())
df["Computer"]=df["Computer"].fillna(df["Computer"].mean())
print("Final missing values\n",df.isnull().sum())

# inserting total score and average score columns
subject=["Maths","Science","English","Social","Computer"]
df.insert(7,"Total score",df[subject].sum(axis=1))
df.insert(8,"Average score",df[subject].mean(axis=1))
print(df)

# calculating grades
df.insert(9,"Grade",np.where(df["Average score"]>=85,'A',np.where(df["Average score"]>=70,'B',np.where(df["Average score"]>=55,'C','D'))))
print(df)

# finding top 3 students
top_3=df.nlargest(3,"Total score")
top_3.to_csv("C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Student-Performance-Analyzer\\data\\toppers.csv",index=False)
print("toppers details are saved as 'toppers.csv'")

# subject wise highest and lowest marks 
subject_summary=pd.DataFrame({
    "Highest marks":df[subject].max(),
    "Lowest marks":df[subject].min()
})
subject_summary.to_csv("C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Student-Performance-Analyzer\\data\\subject_summary.csv")
print("Subject wise maximum and minimum marks are save as 'subject_summary.csv'")

# exporting CSV file               
df.to_csv('C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Student-Performance-Analyzer\\data\\cleanedStudentPerformance.csv',index=False)
print("Data cleaned completed! saved as 'cleanedStudentPerformance.csv")




# ======================
# VISUALIZATIONs
# ======================

# 1.Average marks per subject (Bar chart)
avg_marks=df[subject].mean()
plt.figure(figsize=(8,5))
plt.bar(avg_marks.index,avg_marks.values)
plt.title('Average Marks Per Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Marks')
plt.tight_layout()
plt.savefig('plots/avg_marks_per_subject.png')
plt.show()



# 2.Grade Distribution (pie chart)
grade_counts=df['Grade'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(grade_counts.values,labels=grade_counts.index,autopct='%1.1f%%',startangle=90)
plt.title('Grade Distribution')
plt.tight_layout()
plt.savefig('plots/grade_distribution.png')
plt.show()



# 3.Total Score Distribution (histogram)
plt.figure(figsize=(8,5))
plt.hist(df['Total score'],bins=10)
plt.title('Distribution of Total Score')
plt.xlabel('Total Score')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig('plots/total_score_histogram.png')
plt.show()



# 4. top 10 Students (Bar Chart)
top_10=df.nlargest(10,'Total score')
plt.figure(figsize=(8,5))
plt.bar(top_10['Student_Name'],top_10['Total score'])
plt.title('Top 10 Students by Total Score')
plt.xlabel('Student Name')
plt.ylabel('Total Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/top10_students')
plt.show()