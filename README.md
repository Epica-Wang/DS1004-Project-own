# DS1004-Project
Project 1+2
The goal for this project is to give you hands on experience with analyzing real, big data and apply the concepts you have learned. Each group will select one data collection from a list (see Data Collections below). For the first part of the project, you will analyze the data and generate a descriptive summary of their contents as well as a list of data quality issues. For the second part, you will integrate your selected collection with one or more data sets and look for interesting relationships between the data sets. A list of potentially related data sets is provided below and you are encouraged to look for other data.
Hadoop Stack:  A key component of your project is to get hands-on experience with the techniques you are learning in the course. Therefore, you must use the NYU Cluster and the Hadoop stack. You can choose to write map-reduce, Spark, SparkSQL programs, or any other tools that works on Hadoop or Spark.
 Reproducible results:  All components of your project must be reproducible! Your code must be available on github, and all your analysis results and plots need to be accompanied by the appropriate scripts you used to derive them. Others should be able to reproduce
your results. You should include a README with instruction to run your code and generate the results, plots and visualizations.
Data Collections
1. Transportation
Yellow taxi (2013-2016)
Green taxi (2013-2016)
Download:  http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml
2. Complaints
311 (2009-2016)
Download: (2010-2016)  https://data.cityofnewyork.us/Social-Services/311/wpe2-h2i5
 (2009)  https://data.cityofnewyork.us/Social-Services/new-311/9s88-aed8
3. Crime
NYPD (2006-2016) Download:
 https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i
Part I
To understand the data collection you have selected, you will first explore it and generate a summary of the data. The summary should provide an overview of the data and its contents. For example, a good summary for the Transportation collection can be found at: http://www.nyc.gov/html/tlc/downloads/pdf/2016_tlc_factbook.pdf
(If you select the Transportation collection, your summary must go beyond what is provided in the TLC Fact Book!)
You will also look for data quality issues as well as anomalies. Some questions you should ask include but are not limited to:
- Are there non-empty values that represent missing data (e.g., NULL, N/A, UNSPECIFIED, TBA, (999)999-9999) If so, how many in each column?
- Are there different kinds of values in the same column (e.g., integers and strings)?
- Are there suspicious or invalid values in columns? (e.g., a negative value in a price field;
for spatial data, coordinates outside the city perimeter; an invalid zipcode)
- Are there surprising (or suspicious) events in the data? (e.g., a day with too few taxi trips
or too few noise complaints). Note that you may have to aggregate the data in different ways to search for these events.
Some techniques that may be useful for finding unusual features and outliers include:
     
- Regression Analysis:
Java/Scala:  https://commons.apache.org/proper/commons-math/userguide/stat.html Python:  http://scikit-learn.org/stable/modules/linear_model.html
- Box Plot :
Python:  http://matplotlib.org/examples/statistics/boxplot_demo.html
- Correlation:
- Pearson's Correlation
Java/Scala:  https://commons.apache.org/proper/commons-math/userguide/stat.html
Python:  http://docs.scipy.org/doc/scipy/reference/stats.html
- Mutual Information
Java/Scala:  https://github.com/jlizier/jidt
Python:  http://scikit-learn.org/stable/modules/classes.html
Note: These are just recommendations. You are allowed (and encouraged) to play with other techniques and implementations.
Deliverable:  A report with the data summary and data quality issues submitted to NYU Classes. For each column in the data set, you should provide a script that assigns to each value:
1) a base type (i.e.,  INT/LONG, DECIMAL, TEXT, maybe DATETIME)
2) a semantic data type (e.g., phone, address, city, state, zipcode) -- here, your script could use, e.g., a regular expression to identify phone numbers, a dictionary to check whether a given string is a city.
3) a label from the set [NULL -> missing or unknown information, VALID -> valid value from the intended domain of the column, INVALID/OUTLIER -> suspicious or invalid values]
Note that some columns may have values of multiple types (e.g., telephone, email).
You must include a summary for (1), (2) and (3) in your report. You should include in your summary other data quality issues covered during the 3/27 lecture on data cleaning.
The code/scripts you use in your project must be available in the github repo you provided. You must include a README file with detailed instructions on how to run your code/scripts. Any figures and results in the report must point to the script you used to derived the result. See below for details on the structure of the report.

