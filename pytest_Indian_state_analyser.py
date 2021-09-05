'''
@Author: Javeed
@Date: 2021-09-04
@Last Modified by: Javeed
@Last Modified time: 2021-09-05 01:35:41
@Title : TestCases of Indian_StateCensus_Analyser Using Pytest.
'''
import pytest
import Indian_States_Analyser

# record = Indian_States_Analyser.Indian_States_Analyser.records('StateCode.csv')
# record = Indian_States_Analyser.Indian_States_Analyser.records('StateCensusdata.csv')

def test_record_SC():
    '''
    Description: Function to test the recorded data
    Return: test case pass/file 
    '''
    record = Indian_States_Analyser.Indian_States_Analyser.records('StateCode.csv')
    assert record == 37

def test_record_SCV():
    '''
    Description: Function to test the recorded data
    Return: test case pass/file 
    '''
    record = Indian_States_Analyser.Indian_States_Analyser.records('StateCensusdata.csv')
    assert record == 29

def test_file_type():
    '''
    Description: Function to test the Extension
    Return: test case pass/file 
    '''
    file_type = Indian_States_Analyser.Indian_States_Analyser.extentions('StateCensusdata.csv')
    Expected_file_type = '.csv'
    assert file_type == Expected_file_type
    # file_type_1 = Indian_States_Analyser.Indian_States_Analyser.extentions('StateCensusdata.text')
    # Expected_file_type = '.csv'
    # assert file_type_1 == Expected_file_type

def test_wrong_file_type():
    '''
    Description: Function to test the Extension
    Return: test case pass/file 
    '''
    file_type = Indian_States_Analyser.Indian_States_Analyser.extentions('StateCensusdata.text')
    Expected_file_type = '.csv'
    assert file_type == Expected_file_type

def test_file_name():
    '''
    Description: Function to test the filename
    Return: test case pass/file 
    '''
    file_name = Indian_States_Analyser.Indian_States_Analyser.file_name('StateCensusdata.csv')
    Expected_file_name = 'StateCensusdata.csv'
    assert file_name == Expected_file_name

def test_wrong_file_name():
    '''
    Description: Function to test the filename
    Return: test case pass/file 
    '''
    file_name = Indian_States_Analyser.Indian_States_Analyser.file_name('StateCensus.csv')
    Expected_file_name = 'StateCensusdata.csv'
    assert file_name == Expected_file_name
def test_file_header():
    '''
    Description: Function to test the Headers
    Return: test case pass/file 
    '''
    header = Indian_States_Analyser.Indian_States_Analyser.header('StateCode.csv')
    Expected_header = ['SrNo', 'StateName', 'TIN', 'StateCode']
    assert header == Expected_header
def test_wrong_file_header():
    '''
    Description: Function to test the Headers
    Return: test case pass/file 
    '''
    header = Indian_States_Analyser.Indian_States_Analyser.header('StateCensusdata.csv')
    Expected_header = ['SrNo', 'StateName', 'TIN', 'StateCode']
    assert header == Expected_header

if __name__ == '__main__':
    pytest.main()