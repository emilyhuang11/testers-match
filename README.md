# testers-match

What Is This?
-------------

This is a simple Python/Pandas application intended to process a list of csv files and locate the best tester candidates. Sample csv files (testers.csv, devices.csv, bugs.csv, tester_device.csv) are also provided. The output is testers ranked by the number of the bugs found, based on country and device combination. 

How To Use This
---------------

1. Check if you have Python3 installed. (Run 'python3 --version')
2. If Python3 is not installed, download it from https://www.python.org/downloads/
3. Check if you have Pandas installed. (Run 'pip3 list' to see if Pandas is listed)
3. Run 'pip3 install Pandas' to install Pandas library, if Pandas is not installed
4. Download testersmatch.py file into your running directory. testersmatch.py is under  https://github.com/emilyhuang11/testers-match
5. (Optional) Download sample csv files with 'git clone https://github.com/emilyhuang11/testers-match.git'. This will download sample csv files as well as testermatch.py
5. You need to have all your data csv files (testers.csv, devices.csv, bugs.csv, tester_device.csv) saved in same directory
6. Run 'python3 testersmatch.py' in your running directory


Design Considerations
-------
1. Data from the csv files are preprocessed to speed up the ranking process. As a result, the start up time may be long in the case of large data files. 
2. During data loading, to avoid memory error, a parameter 'blocksize' is used to limit the number of testers that the system will process in each loop.  Instead of creating one single dataframe that contains all 300k+ testers and all the combination of bug/device, only a block of testers is processed in each step. At the end, the results are aggregated. Currently the 'blocksize' is defaulted as 1000, this number can be adjusted depending on the performance testing result. 
3. Python Pandas package is utilized for data merging and filtering. To improve the performance, index is created on column 'country' and 'description', since the ranking is done based on those 2 columns. 

Sample output
-------
Below are sampe test output based on the sample csv files 
1. search with 'us' and 'iphone 4'
```
USR-Emily-Huang:GitRep emily$ Python3 testersmatch.py
Please input data folder:.
Country List (US,GB,JP,ALL. separate by ','):us
Device list (iPhone 4,iPhone 4S,iPhone 5,Galaxy S3,Galaxy S4,Nexus 4,Droid Razor,Droid DNA,HTC One,iPhone 3,ALL. separeate by ','):iphone 4

              name  bugCount
1    Taybin Rutkin        66
0  Miguel Bautista        23
```
2. search with 'US' and ALL

```
USR-Emily-Huang:GitRep emily$ Python3 testersmatch.py
Please input data folder:.    
Country List (US,GB,JP,ALL. separate by ','):US
Device list (iPhone 4,iPhone 4S,iPhone 5,Galaxy S3,Galaxy S4,Nexus 4,Droid Razor,Droid DNA,HTC One,iPhone 3,ALL. separeate by ','):ALL
              name  bugCount
2    Taybin Rutkin       125
1  Miguel Bautista       114
0  Michael Lubavin        99
```

3. search with 'US,  JP' and 'iphone 4s'

```
USR-Emily-Huang:GitRep emily$ Python3 testersmatch.py
Please input data folder:.
Country List (US,GB,JP,ALL. separate by ','):US, JP
Device list (iPhone 4,iPhone 4S,iPhone 5,Galaxy S3,Galaxy S4,Nexus 4,Droid Razor,Droid DNA,HTC One,iPhone 3,ALL. separeate by ','):iphone 4s
              name  bugCount
1    Taybin Rutkin        59
0  Miguel Bautista        26
```
4. search with 'JP' and 'Nexus 4', the csv file is under a specifiied direcory

```
USR-Emily-Huang:GitRep emily$ Python3 testersmatch.py
Please input data folder:/Users/emily/Desktop/tempData
Country List (US,GB,JP,ALL. separate by ','):JP
Device list (iPhone 4,iPhone 4S,iPhone 5,Galaxy S3,Galaxy S4,Nexus 4,Droid Razor,Droid DNA,HTC One,iPhone 3,ALL. separeate by ','):Nexus 4
              name  bugCount
0      Lucas Lowry        25
2  Sean Wellington        23
1   Mingquan Zheng        13

```




