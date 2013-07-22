"""
Function to test connection to the convertapi site
"""


import requests
import base64

API = 275297545
API_URI = "http://do.convertapi.com/word2pdf/json"
filename = 'test.docx'
output = "test.pdf"


def convert():

    payload = {'OutputFileName': output, 'ApiKey': ''}
    files = {'file': open(filename, 'rb')}
    #result={}
    #print(type(result))
    result = requests.post(API_URI, files=files, data=payload)
    #print(type(result))
    #print(result)
    #print('*' * 70)
    #print(result.url)
    #print('*' * 70)
    print(result.headers)
    #print('*' * 70)
    #print(result.text.decode())
    #print('*' * 70)
    print('*' * 70)
    #print (result.json())
    #print('*' * 70)
    pdf = result.json()['File']
    #print(type(pdf))
    #print(pdf)
    pdf = base64.b64decode(pdf)
    #print(pdf)
    f1 = open(output, 'wb')
    f1.write(pdf)
    #print('completed conversion')


if __name__ == "__main__":
    convert()
