
from __future__ import print_function
import json
import requests
import sys
import os

reque = open("input.txt", "r")
reque = reque.read()

#if (sys.version_info > (3, 0)):
#    pass
#else:
#    reload(sys)
#    sys.setdefaultencoding('utf-8')

#arglength = len(sys.argv)

#if arglength <= 2:
#    ruleid = str(100)
#else:
#    ruleid = sys.argv[2]

#if arglength <= 1:
#    print('Please enter the string to translate!')
#    sys.exit(0)
#else:
#    req = sys.argv[1]
#    pass

ip = "127.0.0.1"
port = "5000"
url_root = "/translator"
#print(reque)
url='http://' + ip + ':' + port + url_root + '/translate'
data='[{"src": "' + reque +'", "id": ' + "100" +'}]'

output = requests.post(url, data=data.encode('utf-8')).text

myjson = json.loads(output)
input = myjson[0][0]['src']
output = myjson[0][0]['tgt']

with open('input.txt','r+') as myfile:      
                data = myfile.read()                                                                                              
                myfile.seek(0)                                                                                                    
                myfile.write(output)                                                                                           
                myfile.truncate()   

print(input)
print(output)