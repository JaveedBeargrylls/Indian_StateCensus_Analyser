 
'''
@Author: Javeed
@Date: 2021-08-03 
@Last Modified by: Javeed
@Last Modified time: 2021-09-04 16:21:15
@Title : Indian_States_Analyser.
'''
import csv
import os
from dotenv import load_dotenv
load_dotenv()

class Indian_States_Analyser:
    def records(self,filename):
        '''
        Description: 
                    Function to Records the count
        Parameter: 
                    Filename takes file name as file Input
        Return:
                    Returning the recorded data
            '''
        record = 0
        with open (filename,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_file)
            for row in csv_reader:
                record += 1
        return record

    def extentions(self,filename):
        '''
        Description: 
                Checking of Extension
        Parameter: 
                 filename is parameter which is pass to check the correct file.
        Return: 
                returning the file exists or not
         '''
        file_type = os.path.splitext(filename)
        try:
            if (file_type[1] != '.csv'):
                raise Exception("File type is Not Matched")
            else:
                print('Extention matched',file_type[1])
        except Exception:
                print('Extention is Not Matched')
        return file_type[1]

    def file_name(self,filename):
        '''
        Description:
                    Checking of fileName
        Parameter: 
                    filename takes file name as file Input
        Return:     
                    returning the file type and file exists or not exists
         '''
        try:
            if os.path.isfile(filename):
                print("File is Exists")
                raise Exception("File is found")               
            else:
                print("File is not found")
                raise Exception("File is not found") 
        except :
                print("File is not found")
        return filename

    def header(self,filename):
        '''
        Description: Function to Records the count
        Parameter: filename takes file name as file Input
        Return: returning the recorded data
         '''
        with open (filename,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            list_of_header = []

            for row in csv_reader:
                list_of_header.append(row)
            header = list_of_header[0]
            headers_stateCode = ['SrNo', 'StateName', 'TIN', 'StateCode']
            headers_StateCensusData =  ['State', 'Population', 'AreaInSqKm', 'DensityPerSqKm']
            try:
                if set(header) == set(headers_stateCode):
                    print("Matched")
                    raise Exception("Header Matched")
                elif  set(header) == set(headers_StateCensusData):
                    print("Matched")
                    raise Exception("Header Matched")
                else:
                    return "Header Not Matched"
            except Exception:
                    print("Header Not Found")
        return header

#created dictionary of state code and state name
class State_Census_Analyser(Indian_States_Analyser):
    #code for StateCensusData.csv file
    def state_census_analys(self):
        '''
        Description:
                    Function to append the StateCode to the StateCensusAnalyser and stored in New_Census_file
        Parameter:
                    self to pass
        Return:
                    return the New_Census_file
            '''
        new_states_census_file = []
        filename = 'StateCensusData.csv'
        
        try:
            with open('StateCode.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                dict_state_code = {rows[1]:rows[3] for rows in csv_reader}
        except :
            raise Exception("FileNotFound")
    
        with open(filename,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                    new_states_census_file.append(row)
            print(new_states_census_file)
        for line in new_states_census_file:
            key = line[0]
            try:
                if key in dict_state_code:
                    line.append(dict_state_code.get(line[0]))
                else:
                    raise Exception(KeyError)
            except KeyError:
                print("This Key is not avaiable")
        new_states_census_file[0].append('StateCode')
        print(new_states_census_file)
            
        with open('new_State_Census_file.csv', 'w',newline = '') as new_csv_file:
             writer = csv.writer(new_csv_file)
             writer.writerows(new_states_census_file)

class State_Code(State_Census_Analyser):
    #Code for StateCode.csv file
    def states_code_and_name(self):
        '''
        Description:
                    Function to append the StateCode and StateName to the Dictonary
        Parameter:
                    self to pass
        Return:
                    return the Dictonary of StateCode
            '''
        with open('StateCode.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            dict_state_code = {rows[1]:rows[3] for rows in csv_reader}
            print(dict_state_code)            
  

if __name__ == '__main__':
    
    csv_analyser = State_Code()
    # call record passing file name as state census csv
    # csv_analyser.records('StateCensusData.csv')
    csv_analyser.records(os.getenv('FILE_SCD'))
    # call record passing file name as state code csv
    csv_analyser.records('FILE_SC')
    # check extension passing file name state census csv
    csv_analyser.extentions('FILE_SCD')  
    # check extension passing file name state code csv
    csv_analyser.extentions('FILE_SC') 
    # check header passing state census csv header as list and also state census csv filename 
    csv_analyser.header('FILE_SCD')
    # check header passing state code csv header as list and also state code csv filename
    csv_analyser.header('FILE_SC')
    # get the dict pass
    csv_analyser.states_code_and_name()