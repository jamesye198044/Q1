# -*- coding: UTF-8 -*-
# #!/usr/bin/python

import unittest
from file_process import readfile
from file_process import totalnumber
from file_process import totalsum
import os


class Q1_UnitTest(unittest.TestCase):


    def test01_readfile_normal(self):
    #just test normal input
        filename = 'test.txt'
        result = readfile(filename)
        self.assertEquals(result[13],123)

    def test02_fileNotExist_readfile(self):
    #test when input file not existing
        filename = 'test111.txt'
        self.assertRaises(IOError,readfile,filename)

    def test03_exception_readfile(self):
    #test readfile function can handle the exception liking non-number type in file
        filename = 'test2.txt'
        result = readfile(filename)
        self.assertEquals(result[11],-100)

    def test04_totalnumber(self):
    #test totalnumber function
        list = [000,0,1,2,3]
        result = totalnumber(list)
        self.assertEquals(result,5)

    def test05_totalnumber_nullinput(self):
    #test totalnumber function when input is null
        list = []
        result = totalnumber(list)
        self.assertEquals(result,0)

    def test06_totalsum(self):
    #test totalsum function
        list = [000,0,1,2,3]
        result = totalsum(list)
        self.assertEquals(result,6)

    def test07_totalsum_nullinput(self):
    #test totalnumber function when input list is null
        list = []
        result = totalsum(list)
        self.assertEquals(result,0)

class FunctionTest1_File(unittest.TestCase):

    target_name = 'file_process.py'

    def test_normal_case1(self):
    #just test input file 1

        filename = 'test.txt'
        result = os.popen('python %s %s' % (FunctionTest1_File.target_name,filename)).read()
        self.assertIn('Total number is: 15',result)
        self.assertIn('Total sum is: 138',result)

    def test_normal_case2(self):
    #just test normal input 2

        filename = 'test1.txt'
        result = os.popen('python %s %s' % (FunctionTest1_File.target_name,filename)).read()
        self.assertIn('Total number is: 6',result)
        self.assertIn('Total sum is: 6.3',result)

    def test_normal_case3(self):
    #just test input file 3

        filename = 'test2.txt'
        result = os.popen('python %s %s' % (FunctionTest1_File.target_name,filename)).read()
        self.assertIn('Total number is: 15',result)
        self.assertIn('Total sum is: 111111111111334',result)

    def test_normal_case(self):
    #just test input file is null

        filename = 'test_null.txt'
        result = os.popen('python %s %s' % (FunctionTest1_File.target_name,filename)).read()
        self.assertIn('Total number is: 0',result)
        self.assertIn('Total sum is: 0',result)

    def test_filename_has_space(self):
    #just test the filename has space

        filename = 'te\ st.txt'
        result = os.popen('python %s %s' % (FunctionTest1_File.target_name,filename)).read()
        self.assertIn('Total number is: 15',result)
        self.assertIn('Total sum is: 138',result)

