'''
Created on 22 May 2013

@author: brian
'''
import unittest
from docgeneration import DocGen
import pandoc

#pandoc.PANDOC_PATH = '/usr/bin/pandoc'

class Test(unittest.TestCase):

        def setUp(self):
            self.doc1 = DocGen()

        def tearDown(self):
            pass

        def testImport(self):
            text = self.doc1.importfile('test.txt')
            #print('***************1', text)
            self.assertTrue(text == 'TESTstring')

        def testParseDoc(self):
            #text = self.doc1.importfile('Section2_ContactInformation.xml')
            doc = pandoc.Document()
            text = "<p>hi</p>"
            text = self.doc1.parseDoc(text,'html','markdown')
            #print('***************2', text[:11],'$$$')
            #print(len(text))
            self.assertTrue(text[:11] == "hi\r\n")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testImport']
    unittest.main()
