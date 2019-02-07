# testers-match

==============================

What Is This?
-------------

This is a simple Python/Pandas application intended to process a list of csv files and locate the best tester candidates. Sample csv files (testers.csv, devices.csv and bugs.csv) are also provide. The testers are ranked by the number of the bugs found based on inputting county and device combination. 

How To Use This
---------------

1. Check if you have Python3 installed
2. Check if you have Pandas installed. 
3. Run 'pip3 install Pandas' to install Pandas library
4. Copy files to your running directory
6. Run `python3 TestMatch.py`


Design Considersations
-------
1. Data from the csv files are preprocessed to speed up the ranking process. As a result, the start up time may be long in the case of large data files. 
2. During data loading, to avoid memory error, a parmeter 'granulatiy' is used to limit the number of testers that the system will process in each loop.  Instead of creating one single dataframe that contains all 300k+ testers all the combination of bug/device, only specifed number of testeres were processed in each step. At the end, the reuslts were aggretrated. Currenlty the granulatiy is default as 500, this number can be adjusted depending on the peformance result. 
2. We used Python Pandas package for data merging and filtering, and created index for column 'country' and 'description', since the ranking is done based on these 2 columns. 



