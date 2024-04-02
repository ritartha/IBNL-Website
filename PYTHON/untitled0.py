import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def split_sentence(sentence, separator):
    parts = sentence.split(separator, 1)
    if len(parts) == 1:
        return parts
    else:
        return [parts[0], parts[1].lstrip(separator)]

path = r'C:\Users\Dell\Desktop\html css\PYTHON\Publications.html'

HTMLFile = open(path, "r") 
index = HTMLFile.read()

S = BeautifulSoup(index, 'lxml')

keys = S.findAll('u')

items = S.text.split('\n')

pubs = {}
key = 'none'
paper = []
c = 'none'

for i in range(18,len(items)):
    if len(items[i]) > 1:
        value = []
        
        if items[i] == ' Book Chapter' or len(items[i]) == 5:
            c = 'key'
            key = items[i]
            print('<h2>'+key+'</h2>')
            
        else:
            c = 'value'
            print(items[i])
            
        
        if c == 'value':
            paper.append(items[i])
            pubs.update({key:paper})
        else:
            paper = []
            
            
            
            
            
            
for k in pubs.keys():
    print('<li>')
    print('<h2>'+k+'</h2>') 
    print('<ol>')
    for i in pubs[k]:
        if '    ' not in i:
            i = split_sentence(i, ' ')
            print('<li><p>'+i[-1]+'</p></li>')
    print('</ol>')           
    print('</li>')    
    
 #NEWS

path = r'C:\Users\Dell\Desktop\html css\PYTHON\news.html'   

HTMLFile2 = open(path, "r") 
index = HTMLFile2.read()

S = BeautifulSoup(index, 'lxml')
news = S.findAll('li')


print('<ul>')
for i in news:
    print('<li>'+i.text+'</li>')
print('</ul>')