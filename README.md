# Indian_StateCensus_Analyser

----------

## **In Class**
***parent class State Analyser***
-    *count records in both files*
-    *check extensions to file type csv or text*
-    *check header*

***child class for State Census inheriting state Analyser*** 
-    *create a method to genrate new_csv_file for collect data from both files with comparision i.e.,adding StateCode from StateCode.csv by comparing the stateName from SCD and adding whole data to new CSV file* 

***child class for state code inheriting state analyser*** 
-    *create dict of state code and state name*

----------

## **main**
- *call record passing file name as state census csv* 
- *call record passing file name as state code csv*
- *check extension passing file name state census csv*  
- *check extension passing file name state code csv* 
- *check header passing state_census_csv header as list and also state_census_csv filename* 
- *check header passing state_code_csv header as list and also state_code_csv filename* 

----------

## **Test cases**
- *check with correct file name* 
- *check with worng filename* 
- *check with right record count*
- *check with wrong record count*
- *check with right extension* 
- *check with wrong extension*
- *check with right header*
- *check with wrong header*
### Implement the above testcases using pytest
### Created a new json file by converting the new_State_census to a JSON
