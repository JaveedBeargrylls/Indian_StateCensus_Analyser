  
'''
@Author: Javeed
@Date: 2021-09-02
@Last Modified by: Javeed
@Last Modified time: 2021-09-04 21:10:05
@Title : TestCases of Indian_StateCensus_Analyser.
'''
from Indian_States_Analyser import Indian_States_Analyser
import unittest
import Indian_States_Analyser

class TestAnalyser(unittest.TestCase):
    def test_records_State_Analyser(self):
        '''
        Description: Function to test the recorded data
        Return: test case pass/file 
        '''
        self.assertEqual(Indian_States_Analyser.Indian_States_Analyser.records('statecensusdata.csv'),29)      
        self.assertEqual(Indian_States_Analyser.Indian_States_Analyser.records('statecensusdata.csv'),30)
        
    def test_records_States_code(self):
        '''
        Description: Function to test the recorded data
        Return: test case pass/file 
        '''
        try:
            self.assertEqual(Indian_States_Analyser.Indian_States_Analyser.records('statecode'),30)       
            self.assertEqual(Indian_States_Analyser.Indian_States_Analyser.records('statecode'),37)
        except Exception:
            print("Error expected at Records at CSV_States code")   

    def test_file_name(self):
        '''
        Description: Function to test the filename
        Return: test case pass/file 
        '''
        self.assertEqual(Indian_States_Analyser.State_Code.file_name(self,'statecode.csv'),'statecode.csv')
        self.assertEqual(Indian_States_Analyser.State_Code.file_name(self,'statecode.csv'),'sample.csv')  
        
        #same test case used assertraise
        with self.assertRaises(Exception):
            self.assertEqual(Indian_States_Analyser.State_Code.file_name(self,'statecode.csv'),'statecode.csv')
            self.assertEqual(Indian_States_Analyser.State_Code.file_name(self,'statecode.csv'),'sample.csv')    
    def test_file_type(self):
        '''
        Description: Function to test the Extension
        Return: test case pass/file 
        '''
        self.assertEqual(Indian_States_Analyser.State_Code.extentions(self,'statecensusdata.csv'),'statecensusdata.text')
        self.assertEqual(Indian_States_Analyser.State_Code.extentions(self,'stateCode.csv'),'statecode.csv')    

        with self.assertRaises(Exception):
            self.assertEqual(Indian_States_Analyser.State_Code.extentions(self,'statecensusdata.csv'),'statecensusdata.csv')
            self.assertEqual(Indian_States_Analyser.State_Code.extentions(self,'stateCode.csv'),'statecode.text')    

    def test_header(self):
        '''
        Description: Function to test the Headers
        Return: test case pass/file 
        '''
        expected_state_code = ['SrNo', 'StateName', 'TIN', 'StateCode']
        expected_state_census = ['State', 'Population', 'AreaInSqKm', 'DensityPerSqKm']
        with self.assertRaises(Exception):
            self.assertEqual(Indian_States_Analyser.State_Code.header(self,'statecode.csv'),expected_state_code)
            self.assertEqual(Indian_States_Analyser.State_Code.header(self,'statecensusdata.csv'),expected_state_code)
            self.assertEqual(Indian_States_Analyser.State_Code.header(self,'statecode.csv'),expected_state_census)
            self.assertEqual(Indian_States_Analyser.State_Code.header(self,'statecensusdata.csv'),expected_state_census)

if __name__ == '__main__':
    unittest.main()
    