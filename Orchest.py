#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#In order to fully grasp what is going on please read the annotation.
#Please also open the Flow diagram (). It will make more sense that way :)
#from jurrasicapicall import JurrasicCall  #imports our api call function

input = open("input.txt", "r")
##############################################################################################################################################################################
# From here we are moving into the JurrasicAPI
##############################################################################################################################################################################

from googletrans import Translator                                #Translator from google, which checks what language it is (should be approved first)
detector = Translator()                                           
    
readinput = input.read()
languagein = detector.detect(readinput)                               #Sets languagein as the langauge which is used in 'input' 
print("The detected language is: ", languagein.lang)
#print("the input given is: ", input)
givenlang = languagein.lang



print("languagemodelactive")
if givenlang == "en":                                         #if the language is english
    #outputJur = JurrasicCall(readinput)                                 #...it will call the Jurrasic API and generate an answer
    exec(open("jurrasicapicall.py").read())
    jurrasicoutput = open("jurrasicoutput.txt", "r")
    jurrasicoutput = jurrasicoutput.read()
        
    print(jurrasicoutput)
else:
#      #TranslateDutch-English                                                                                                               #Needs to be implemented                                                  
    exec(open("oeat-onmtpost.py").read())
#        !onmt_translate --model Flipped_model_retry_step_100000.pt --src input.txt --output Du-EnOutput.txt --gpu 0 -verbose
    g = open("Input.txt", "r")                                                                                 #Opens the output (from our translation) as read
    TranslatedInput = g.read()                                                                                                           #Sets TranslatedInput to the output which was generated by our model
    exec(open("jurrasicapicall.py").read())
    jurrasicoutput = open("jurrasicoutput.txt", "r")
    jurrasicoutput = jurrasicoutput.read()
    print(jurrasicoutput)


if languagein.lang == "en":     
  jurrasicoutput = jurrasicoutput
else:                                                                                                               #When input was dutch, the output has to be translated back to dutch.
  exec(open("oeat-onmtpostBack.py").read())                                                                                                 #Empties the rest of the file (except for the stuff which was just added) 
  #!onmt_translate --model /content/gdrive/MyDrive/Software_Engineering/CodeRelated/Translation/EN-NL/model/model_retry_step_100000.pt --src /content/gdrive/MyDrive/Software_Engineering/CodeRelated/Orchestrator/input.txt --output /content/gdrive/MyDrive/Software_Engineering/CodeRelated/Orchestrator/output.txt --gpu 0 -verbose
  f = open("Du-EnOutput.txt", "r")                 #Opens the output as read
  TranslatedOutputJur = f.read()                                                                                    #Sets TranslatedOutput to the output which was generated by our model
  jurrasicoutput = TranslatedOutputJur
  print(jurrasicoutput)  
  #send to interface            

