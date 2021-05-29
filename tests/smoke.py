'''
Created on May 29, 2021

@author: mballance
'''
from unittest.case import TestCase
import yaml
from yaml_srcinfo_loader.loader import Loader
from _io import StringIO

class Smoke(TestCase):
    
    def test_file_lineno(self):
        with open("file.txt", "w") as fp:
            fp.write("Hello World!\n")
        
        with open("file.txt", "r") as fp:
            print("fp.name=" + str(fp.name))
            
    def test_scalar(self):
        doc = """
        a:
          - b: 5
          - c: 7
        """
        
        stream = StringIO(doc)
        stream.name = "myfile1"
        
        y = yaml.load(stream, Loader=Loader)
        
        print("y: " + str(y))