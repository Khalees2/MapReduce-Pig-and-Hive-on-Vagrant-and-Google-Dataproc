# Large-Data-Analysis-using-MapReduce-Pig-and-Hive-on-Vagrant-and-Google-Dataproc

The below tasks are done in both Vagrant and Google Dataproc. 

Vagrant Setup: Please see Hive_Metastore_Error_fix repository.

# Tasks:
Using MapReduce/Pig/Hive as required, carry out the following tasks:
1. Acquire the top 200,000 posts by viewcount from StackExchange Data archive(http://data.stackexchange.com/stackoverflow/query/new)
2. Using pig or mapreduce, extract, transform and load the data as applicable
3. Using hive and/or mapreduce, get:
   * The top 10 posts by score
   * The top 10 users by post score
   * The number of distinct users, who used the word ‘hadoop’ in one of their posts
     Using mapreduce calculate the per-user TF-IDF(op 10 terms for each of the top 10 users by post score, as returned from        task2)
