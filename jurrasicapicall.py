#!/usr/bin/env python
# coding: utf-8

# In[9]:




import requests
import json
    
#Reads the input.txt (where the input question is stored, either directly after interface or after NL-EN translation)    
input = open("input.txt", "r")
RequestJurrasic = input.read()

#Calls Jurassic API    
new = requests.post(
      "https://api.ai21.com/studio/v1/j1-jumbo/complete", #sends our request ot the ai21 servers
      headers={"Authorization": "Bearer vc7KLlGzEjqrbyKuJ5lmJXejJCeBVfE2"}, #authorizes use with personal authorization code
      json={
          "prompt": RequestJurrasic,  #Request prompt
          "numResults": 1,  #number of different results it will return
          "maxTokens": 8,   #max lenght of sentence
          "stopSequences": [".", "?", " ?"], #stops whenever it generates a . This will make sure that it doesn't print extra words after the first sentence. (so that it wont print: Jackie Chan #is the best actor. He (and then not continue this sentence, because it ran out of tokens)
          "topKReturn": 0,    #If higher, it won't look at the best results, but rather the third best or 4th best (according to K)
          "temperature": 0.0  #How well will the responses fall within the "trained response". Increasing this will result in the responses being more off-topic
      }
  )

data = new.json()   #stores the response from ai21 into the variable data
for a in data["completions"]: #reads out the json 
    newdata = a               #unpacks json into multidimensional list
    
#Removes enters from input data.
newnewdata = ""
for b in newdata["data"]["text"]:
    if b != "\n":
        newnewdata += b
        
   
#Saves Jurassic output to jurrasicoutput.txt    
with open('jurrasicoutput.txt','r+') as myfile:      #Opens input file
    data = myfile.read()                                                                                              
    myfile.seek(0)                                                                                                    
    myfile.write(newnewdata)                                                                                           
    myfile.truncate()   





