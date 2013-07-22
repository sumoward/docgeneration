'''
Created on 22 May 2013

@author: brian
'''
import pandoc
from bs4 import BeautifulSoup

import webbrowser
import urllib.request
import codecs
from mailmerge import MailMerge
import subprocess
import shutil

#pandoc.PANDOC_PATH = PANDOC_PATH = 'C:/pandoc/pandoc'


class DocGen:

    def importfile(self, filename):
        f = open(filename, "r")
        text = f.read()
        #print (text)
        return text

    def parseDoc(self, text, input_type, output_type):
        #print('output_type', output_type)
        self.doc = pandoc.Document()
        #print('*INPUT=', text)
        if input_type == 'markdown':
            self.doc.markdown = text
        elif input_type == 'html':
            self.doc.html = text
        if output_type == 'html':
            print('html')
            result = self.doc.html
        elif output_type == 'rst':
            print('rst')
        elif output_type == 'markdown':
            print('markdown')
            result = self.doc.rst
        #print ('*OUTPUT=', result)
        #save it as a pdf
        #doc.to_file('principal.pdf')
        return(result)
#
#    def create_pdf(self, text):
#
#        self.doc.to_file('principal1.pdf')
#        #self.doc.to_file('principal1.docx')

#    def scrape_url(self, url):
#
#        #print(url)
#        #open the page in a browser to allow verification
#        #webbrowser.open(url)
#        #open the url
#        holder = urllib.request.urlopen(url)
#        #use soup to parse the data
#        soup = BeautifulSoup(holder)
#
#        #print('SOUP HERE++++++++++++++++++++++++++++++++++++')
#        #print(soup.prettify())
##        holder = open('parsedata.txt', 'w')
##        holder.write(soup.prettify())
#        #print("File updated with soup")
#        return soup
##    
#    def change_encoding(self,file):
#        
#        holder1 ='holder1.txt'
#        holder2 ='holder2.txt'
#        f1 = open(holder1,'w' )
#        f1.write(file)
#        
#        result = ''
#        sourceEncoding = "iso-8859-1"
#        targetEncoding = "utf-8"
#        file = codecs.open(holder1, "r", sourceEncoding)
#        
#        contents = file.read()
#        target = codecs.open(holder2, "w", targetEncoding)
#        target.write(contents)
#        f2 = open(holder2, 'r')
#        result = f2.read()
#        return result

    def mail_merge(self, company_name):

        #template1 = 'test1.docx'
        template2 = 'Executive_Summary2.docx'

        document = MailMerge(template2)
        print (document.get_merge_fields())
        #merge fields
        #{'ZIP_Code', 'Address_Line_2', 'Country_or_Region',
        #'Address_Line_1', 'Company_Name', 'Title',
        # 'State', 'City', 'First_Name', 'Work_Phone',
        #'Email_Address', 'Home_Phone', 'Last_Name'}

        document.merge(Title = 'Mr',
                        First_Name ='Joe',
                        Last_Name = 'OShea',
                        Company_Name = 'Principal Systems',
                        Email_Address= 'joeoshea@principalsystems.com',
                        City = 'Dublin',
                        State = 'Dublin',
                        Work_Phone ='123333',
                        Address_Line_1 ='56 Pembrooke road',
                        Address_Line_2='Ballsbridge',
                        Home_Phone='1234567',
                        Country_or_Region='Ireland',
                        ZIP_Code = 'Dublin6')

        output = company_name + '_output.docx'
        document.write(output)
        return  output
    
#    def convert_pdf(self):
#
#        input_filename = 'test1.docx'
#        output_filename = 'output.pdf'
#
#        p = subprocess.Popen(['unoconv', '--stdout', input_filename], stdout=subprocess.PIPE)
#        with open(output_filename, 'w') as output:
#            shutil.copyfileobj(p.stdout, output)







if __name__ == "__main__":
    print('test  dopcument generation')
    doc2 = DocGen()
    company_name = 'Principal Systems'
    #output_type = 'html'
    
    #doc2.parseDoc(text, input_type, output_type)
    
    
#    print('Begin mail merge for ', company_name)
#    company_data = {'Title' : 'Mr',
#                        'First_Name' :'Joe',
#                        'Last_Name' : 'OShea',
#                        'Company_Name' : 'Principal Systems',
#                        'Email_Address': 'joeoshea@principalsystems.com',
#                        'City' : 'Dublin',
#                        'State' : 'Dublin',
#                        'Work_Phone' :'123333',
#                        'Address_Line_1' :'56 Pembrooke road',
#                        'Address_Line_2':'Ballsbridge',
#                        'Home_Phone':'1234567',
#                        'Country_or_Region':'Ireland',
#                        'ZIP_Code' : 'Dublin6'}
#
#    filename = doc2.mail_merge(company_name)

    print('end of test')

