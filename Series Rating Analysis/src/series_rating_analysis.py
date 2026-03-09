import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#loading csv file
df=pd.read_csv("C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Series-Rating_Analysis\\data\\series_rating_dataset.csv")
print(df.head())

# required columns
df_series=df[["Series_Title","Genre","Rating","No_of_Votes"]]
print(df_series.head())

# handling missing values
print("Missing values:")
print(df_series.isnull().sum())

# exploding genre column
df_series["Genre"]=df_series["Genre"].str.split(", ")
df_series=df_series.explode("Genre")

# top rated series for each genre
top_rated_series=df_series.loc[(df_series.groupby("Genre")["Rating"].idxmax())]
top_rated_series.to_csv("C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Series-Rating_Analysis\\data\\top_rated_series_inEachGenre.csv")
print("top rated series are saved as 'top_rated_series_inEachGenre.csv'")


# calculating weighted rating
df_series["Weighted Rating"]=df_series["Rating"]*df_series["No_of_Votes"]
print(df_series.head())

# top weighted Series
top_weighted_series=(df_series.sort_values("Weighted Rating",ascending=False).drop_duplicates("Series_Title").head(10))
top_weighted_series.to_csv("C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Series-Rating_Analysis\\data\\top10_weighted_series.csv",index=False)
print("top_weighted_series are saved as 'top_weighted_series.csv'")

# Rating anomalies
mean_rate=df_series["Rating"].mean()
std_rate=df_series["Rating"].std()
lower_bound=max(0,mean_rate - 2*std_rate)
upper_bound=mean_rate + 2*std_rate
print(mean_rate,std_rate,lower_bound,upper_bound)
df_series["Rating Anomalies"]=np.where((df_series["Rating"] < lower_bound)  | (df_series["Rating"] > upper_bound),"Yes","No")


# exporting csv file
df_series.to_csv("C:\\Users\\soumy\\OneDrive\\Documents\\Python_lib\\projects\\Series-Rating_Analysis\\data\\cleanedSeriesRatingDataset.csv",index=False)
print("dataset is cleaned! saved as 'cleanedSeriesRatingDataset.csv'")




# ======================
# VISUALIZATION
# ======================

# 1. top 10 series by Weighted ratring (bar chart)
plt.figure(figsize=(10,8))
plt.barh(top_weighted_series['Series_Title'],top_weighted_series['Weighted Rating'],color='purple')
plt.title('Top 10 Series by Weighted Rating')
plt.xlabel('Weighted Ratings')
plt.ylabel('Series Title')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('plots/top10_series_by_Weighted_Rating.png')
plt.show()



# 2. Average Rating by Genre
avg_rating_genre=df_series.groupby('Genre')['Rating'].mean().sort_values(ascending=False)
plt.figure(figsize=(10,6))
plt.bar(avg_rating_genre.index,avg_rating_genre.values,color='Green')
plt.title('Average Rating by genre')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('plots/avg_rating__by_genre.png')
plt.show()


# 3. distribution of Ratings

plt.figure(figsize=(8,6))
plt.hist(df_series['Rating'],bins=20,edgecolor='black')
plt.title('Distibution of Series Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Series')
plt.tight_layout()
plt.savefig('plots/distribution_of_ratings.png')
plt.show()


# 4. votes vs Rating (scatter plot)
plt.figure(figsize=(8,6))
plt.scatter(df_series['No_of_Votes'],df_series['Rating'],alpha=0.5)
plt.title('Votes vs Rating')
plt.xlabel('Number of Votes')
plt.ylabel('Rating')
plt.tight_layout()
plt.savefig('plots/votes_vs_rating_scatter_plot.png')
plt.show()