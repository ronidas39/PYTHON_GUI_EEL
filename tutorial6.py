import eel
import requests
import base64
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import gridfs
import datetime
import csv
import urllib
import io
from PIL import Image
from pymongo import MongoClient
client=MongoClient("mongodb+srv://"+"ronidas"+":"+urllib.parse.quote("Rambo@1234")+"@cluster0-lymvb.mongodb.net/test?retryWrites=true&w=majority")
db=client["whatsapp_db"]
#upload file
fs = gridfs.GridFS(db)
eel.init("HTMLS")
@eel.expose
def upload(data):
    data=data.split(",")[1]
    
    
    decode_data=base64.b64decode(data,validate=True)
    
    with open("cv112.pdf","wb")as f1:
        f1.write(decode_data)
        f1.close()
    fs = gridfs.GridFS(db)
    with open('cv112.pdf','rb') as f2:
        data=base64.b64encode(f2.read())
    
    with fs.new_file(chunkSize=800000,filename="sample111.pdf")as fp:
        fp.write(data)

    x=fs.find_one({'filename':'sample111.pdf'})
    print(x)
   
    #data=base64.b64decode(data,validate=True)
    with open("cv115.pdf","wb")as f1:
        f1.write(base64.b64decode(x.read()))
        f1.close()
    print("done")  


  
 
  

    


eel.start("tutorial6.html",size=(1024,950))