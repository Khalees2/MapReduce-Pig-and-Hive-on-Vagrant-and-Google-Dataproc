# Large-Data-Analysis-using-MapReduce-Pig-and-Hive-on-Vagrant-and-Google-Dataproc

The below tasks are done in both Vagrant and Google Dataproc. 

Vagrant Setup: Please see Hive_Metastore_Error_fix repository.

# Tasks:
Using MapReduce/Pig/Hive as required, carry out the following tasks:
1. Acquire the top 200,000 posts by viewcount from StackExchange Data archive(http://data.stackexchange.com/stackoverflow/query/new)

Stack Overflow's data is extracted from SE by querying on the table POSTS. It has 22 columns and viewCount is one of the columns. We have analysed 200000 records in this work. It is possible to fetch only 50000 records per query so, we obtained four separate csv files by running four queries to obtain the top 200000 records ordered by viewCount in descending order. The queries are provided along with this report in the file named "DataAcquisition.txt". It is necessary to clean the data to load it into Pig. So, we made use of Python 3.7.1 [6] with pandas and re (regular expressions) libraries to clean the data. HTML tags, new-line characters, commas, and special characters are removed from Body and Title columns using Regular expressions. Four csv files are then merged to a single file named "final.csv". The source code for the same is submitted along with the report.

2. Using pig or mapreduce, extract, transform and load the data as applicable

A. Pig Usage

Apache Pig has a Java repository to support User Defined Functions(UDF) called Piggybank. It is a jar file where useful functions for data loading has been written in Java, this Jar file should be registered by specifying the path of the directory where it resides. Once it is registered, we can use any functions defined in the Jar. We can register the jar files with the following syntax "REGISTER <path> ". After registering the UDF, it is a good practice to define the function alias that we want to use. We can specify the alias name with the "DEFINE" keyword. Before we start loading the data into Pig it is mandatory to make sure all necessary Hadoop Daemons are up and running. We can use command "jps" to check if the daemons have
started. Basic Hadoop commands are provided in a file named "HadoopCommands.txt". The LOAD operator can be used to load the input data which is stored in the local or Hadoop directory. We have used CSVExcelStorage defined in Piggybank jar.
Null values in the Body and Title fields of the table are removed using the Pig FILTER operator. Once Null values are removed, we can select the necessary columns or fields required into a new relation and then it can be stored into local or Hadoop directory using STORE Keyword. The Pig script used for this work is submitted in the file named "PigScripts.txt".

B. Hive Usage

Apache Hive is SQL like querying language which facilitates querying of large datasets. In this work, the data stored in the Hadoop directory which is the output of Pig explained earlier is loaded directly into the Hive table while creating. Once the data is loaded into hive tables, we can start querying on the tasks mentioned as a part of this work.


3. Using hive and/or mapreduce, get:
   * The top 10 posts by score
   * The top 10 users by post score
   * The number of distinct users, who used the word ‘hadoop’ in one of their posts
     Using mapreduce calculate the per-user TF-IDF(op 10 terms for each of the top 10 users by post score, as returned from        task2)
     
The first three tasks are performed using Hive. Please see the report for Hive queries. The Hive Queries are submitted in the file named "HiveQueries.txt".

As the result of Task two we will get the top ten users by post score and for each of these users we need to find out the top 10 terms used by each one of them by calculating tf-idf, This is the Task four. A new table called TFIDF is created to store the results of Task two which will give the top 10 users. By selecting each user from the TFIDF table, Body and Title content of each post of each of the top ten users is extracted and stored into text file <userId>.txt format where userId represents each user. So, we have now ten text files of the top ten users containing Body and Title data. These ten text files are provided as inputs for tf-idf calculation using MapReduce. Python 2.7.12 is used to calculate tf-idf. Four mapper functions, three reducer functions are used for this task, the Source code for this task can be found in this repo.
  
# Google Dataproc
Google Cloud platform offers a public service for the analysis of Big Data called Cloud Dataproc [10].
This platform comprises of a wide variety of public offerings for running Apache Hadoop clusters and
Apache Spark. It is simple, cost-effective and quick solutions for Big Data analysis where anybody can
create and launch clusters within a few minutes. It provides many open source technologies such as Hive,
Pig, Spark, and others for Extract, Transforms and Load processes. In this work, I created a single node
cluster consisting of 4 vCPUs and a storage capacity of 20GB. Task one, two and three are executed in the
Dataproc. Due to the limitation of space, screenshots are not attached in this report. Screenshots are provided
along with report separately.

# Report with Screenshots
Please see the report for detailed analysis of results with screenshots
