import pandoc
doc = pandoc.Document()
doc.markdown = '''#I am an Heading Tag
* bullet point
* hello joe1
* point with [link](http://www.principalsystems.com/)!
'''
print (doc.rst)
#print('here*********************')
holder = doc.docbook
print (holder)
doc.to_file('test2.pdf')
