🎬 Series Rating Analysis
📌 Project Overview
This project analyzes series ratings using Python, Pandas, NumPy, and Matplotlib.
The analysis focuses on:
•	Understanding genre-wise performance
•	Identifying top-rated and top-weighted series
•	Visualizing rating patterns
•	Detecting rating anomalies using statistical methods
________________________________________
📂 Dataset Description
The dataset contains the following key columns:
•	Series_Title
•	Genre (multiple genres per series)
•	Rating
•	No_of_Votes
Note:
Each series may belong to multiple genres, which are processed during the data analysis.
________________________________________
🎯 Problem Statement
The goal of this project is to analyze series ratings to:
•	Identify the top-rated series for each genre
•	Calculate weighted ratings considering both ratings and vote counts
•	Find the Top 10 series based on weighted ratings
•	Detect series with unusually high or low ratings (rating anomalies)
•	Visualize rating trends and popularity patterns
________________________________________
🛠 Technologies Used
•	Python
•	Pandas
•	NumPy
•	Matplotlib
________________________________________
📚 Concepts Applied
This project applies several important data analysis concepts:
•	Data selection and cleaning
•	String operations (str.split)
•	Data normalization using explode()
•	Grouping and aggregation (groupby)
•	Index-based filtering (idxmax)
•	Weighted rating calculation
•	Statistical anomaly detection (mean ± 2 × standard deviation)
•	Sorting and duplicate handling
•	Data visualization using Matplotlib
•	Exporting processed data to CSV files
________________________________________
⚙️ Steps Performed
1.	Loaded the dataset using Pandas
2.	Selected the required columns for analysis
3.	Split multiple genres and normalized the data using explode()
4.	Identified top-rated series for each genre
5.	Calculated weighted ratings using ratings and vote counts
6.	Extracted the Top 10 series based on weighted ratings
7.	Detected rating anomalies using statistical thresholds
8.	Created visualizations to present insights
9.	Exported cleaned and analyzed datasets
________________________________________
📊 Visualizations Included
The project includes the following charts:
•	Top 10 Weighted Series (Bar Chart)
•	Average Rating by Genre (Bar Chart)
•	Rating Distribution (Histogram)
•	Votes vs Rating (Scatter Plot)

These visualizations help understand:
•	Which series perform the best
•	Which genres receive higher ratings
•	How ratings are distributed
•	The relationship between popularity (votes) and ratings
________________________________________
📈 Output Files
The project generates the following output files:
•	cleanedSeriesRatingDataset.csv → Cleaned dataset
•	top_rated_series_inEachGenre.csv → Top-rated series in each genre
•	top10_weighted_series.csv → Top 10 series based on weighted rating
•	Chart images (.png) → Visual insights from the analysis
________________________________________
🏁 Conclusion
This project demonstrates practical data analysis and visualization skills using Pandas, NumPy, and Matplotlib.
It covers:
•	Data cleaning
•	Aggregation
•	Statistical analysis
•	Data visualization
These are core skills required for Data Analyst roles.

