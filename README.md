Introduction

This repository contains source code for the assignments of Udacity's course, Introduction to Hadoop and MapReduce, which was unveiled on 15th November, 2013.
This is a short course by Cloudera guys in association with Udacity. Instructors for this course are Sarah Sproehnle and Ian Wrigley, both from Cloudera and Gundega Dekena, Course Developer is from Udacity.

Course does not mandate any programming language for writing Hadoop MapReduce jobs; but they have mainly used / taught Hadoop MapReduce jobs using Python [i.e. with Hadoop Streaming approach for running jobs] during the course.

I have developed Hadoop MapReduce code for the 2 problem statements [3 questions each] in 2 programming languages; Python as well as Java.
Instructions for Virtual Machine download and setup

Please refer instructions document provided by Course Instructors for details on the Hadoop Virtual Machine [VM henceforth] setup required for running these examples.
As mentioned in the above document, VM image with Hadoop installed and preconfigured, can be downloaded from Udacity CDN.

Please be forewarned, the size of this compressed VM archive is 1.7 GB. Also it does not uncompress with either 7-Zip or Windows default Zip utility. You might have to use WinRAR or WinZip or even Cygwin unzip to uncompress the same, if you are on a Windows platform. On other Operating Systems, probably unzip command might work just fine. Uncompressed size of this VM is 4.2 GB.

Credentials to login to this Virtual Machine are: training / training. You will not need root access for any of the assignments of this Course. But just in case if you need, the password for root is training.

Please ensure that you configure the VM to at least 1.5 GB of RAM in VMware Player. It might run much better with 2 GB though. I have used VMware Player v5.0.2, the current latest version as of this writing [i.e. 28th November, 2013] is v6.0.1.
Data
Input Files
These input compressed archives can also be downloaded from Udacity servers. Please check here for input file for Problem Statement 1 and here for Problem Statement 2.
These links are also mentioned in the instructions document provided by Udacity Course Instructors.

Problem Statement1

Execution steps are also documented for running the following in Python.
Question#1

Instead of breaking the sales down by store, instead give us a sales breakdown by product category across all of our stores.

    What is the value of total sales for the following categories?
        Toys
        Consumer Electronics
Code : Mapper.py and Reducer.py

Question#2

Find the monetary value for the highest individual sale for each separate store.

    What are the values for the following stores?
        Reno
        Toledo
        Chandler
Code : Mapper1.py and Reducer1.py

Question#3

Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

    Find
        Total sales value across all the stores
        Total number of sales
Code : Mapper2.py and Reducer2.py

Problem Statement2:

Execution steps are also documented for running the following in Python 

Question#1

Write a MapReduce program which will display the number of hits for each different file on the Web site.

    Find
        How many hits were made to the page: /assets/js/the-associates.js?

Code : Mapper3.py and Reducer3.py
