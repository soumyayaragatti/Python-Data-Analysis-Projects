🎬 Series Rating Analysis
📌 Project Overview

This project analyzes series ratings using Python, Pandas, NumPy, and Matplotlib.
The analysis focuses on understanding genre-wise performance, identifying top-rated and top-weighted series, visualizing rating patterns, and detecting rating anomalies using statistical methods.

📂 Dataset Description

The dataset contains the following key columns:
Series_Title
Genre (multiple genres per series)
Rating
No_of_Votes
Each series may belong to multiple genres.

🎯 Problem Statement

Analyze series ratings to:
Identify the top-rated series for each genre
Calculate weighted ratings considering both ratings and vote counts
Find the top 10 series based on weighted ratings
Detect series with unusually high or low ratings (rating anomalies)
Visualize rating trends and popularity patterns

🛠 Technologies Used

Python
Pandas
NumPy
Matplotlib

📚 Concepts Applied

Data selection and cleaning
String operations (str.split)
Data normalization using explode()
Grouping and aggregation (groupby)
Index-based filtering (idxmax)
Weighted rating calculation
Statistical anomaly detection (mean ± 2×std)
Sorting and duplicate handling
Data visualization using Matplotlib
Exporting data to CSV files

⚙️ Steps Performed

Loaded the dataset using Pandas
Selected required columns for analysis
Split multiple genres and normalized data using explode()
Identified top-rated series for each genre
Calculated weighted ratings using ratings and votes
Extracted top 10 series based on weighted ratings
Detected rating anomalies using statistical thresholds
Created visualizations for better insights
Exported cleaned and analyzed datasets

📊 Visualizations Included

Top 10 Weighted Series (Bar Chart)
Average Rating by Genre (Bar Chart)
Rating Distribution (Histogram)
Votes vs Rating (Scatter Plot)
These charts help understand:
Which series perform best
Which genres are highly rated
How ratings are distributed
Relationship between popularity and rating

📈 Output Files

cleanedSeriesRatingDataset.csv → Cleaned and processed dataset
top_rated_series_inEachGenre.csv → Top-rated series per genre
top10_weighted_series.csv → Top 10 series based on weighted rating
Chart images (.png) for visual insights

🏁 Conclusion

This project demonstrates practical data analysis and visualization skills using Pandas, NumPy, and Matplotlib.
It covers data cleaning, aggregation, statistical analysis, and visual storytelling—key skills required for data analyst roles.
