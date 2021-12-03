import json
import requests
import sys
import os

#Opens input.txt
reque = open("input.txt", "r")
reque = reque.read()

#Host pc ip adress
ip = "192.168.2.127"
#Port
port = "5000"
url_root = "/translator"
#Saves request adress to url
url='http://' + ip + ':' + port + url_root + '/translate'
#Saves the data and the specific model to data (100 means NL-EN)
data='[{"src": "' + reque +'", "id": ' + "100" +'}]'
#Gets output from Host pc
output = requests.post(url, data=data.encode('utf-8')).text

#Unpack Json
myjson = json.loads(output)
input = myjson[0][0]['src']
output = myjson[0][0]['tgt']

#Removes enters from input data.
newnewdata = []
for b in output:
    if b != "\n":
        newnewdata.append(b)
        
#Removes glitch in tokenization, where the last questionmark doesn't get detokenized.
if newnewdata[-1] == "?" and newnewdata[-2] == " ":
    del newnewdata[-2]
processeddata = ""
for c in newnewdata:
    processeddata += c
    
#Saves Json in input.txt (So that the JurassicAPIcall only needs to check 1 file for input, and previous input is no longer necessary)
with open('input.txt','r+') as myfile:      
                data = myfile.read()                                                                                              
                myfile.seek(0)                                                                                                    
                myfile.write(processeddata)                                                                                           
                myfile.truncate()   

#Sends results to Interface
print("Translated input: ", processeddata)