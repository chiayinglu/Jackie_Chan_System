import json
import requests
import sys
import os

reque = open("jurrasicoutput.txt", "r")
reque = reque.read()


#Host pc ip adress
ip = "192.168.2.127"
#Port
port = "5000"
url_root = "/translator"
#Saves request adress to url
url='http://' + ip + ':' + port + url_root + '/translate'
#Saves the data and the specific model to data (101 means EN-NL)
data='[{"src": "' + reque +'", "id": ' + "101" +'}]'
#Gets output from Host pc
output = requests.post(url, data=data.encode('utf-8')).text

#Unpack Json
myjson = json.loads(output)
input = myjson[0][0]['src']
output = myjson[0][0]['tgt']
#Saves Json in Du-EnOutput (NL-EN output)
with open('Du-EnOutput.txt','r+') as myfile:      
                data = myfile.read()                                                                                              
                myfile.seek(0)                                                                                                    
                myfile.write(output)                                                                                           
                myfile.truncate()   


#print(output)