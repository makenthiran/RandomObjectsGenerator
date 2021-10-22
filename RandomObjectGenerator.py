"""
Created on Thu Oct 21 23:30:35 2021

@author: mahendran.pp
"""

import random
import math
import time
import os
from flask import Flask
from flask import send_file

app = Flask(__name__)

alphanumeric =  'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

generatedInput = {
        'alphanumeric' : 0,
        'alphabets' : 0,
        'integer' : 0,
        'realnumber' :0,
        'fileName':''
}

#reset the value for new random generate request
def default_input():
    global generatedInput
    generatedInput = {
        'alphanumeric' : 0,
        'alphabets' : 0,
        'integer' : 0,
        'realnumber' :0,
        'fileName':''
    }

def generateAlphaNumeric(length):
    randomString = ''
    for i in range(length):
        randomString += alphanumeric[random.randint(0,61)]
    return randomString

def generateAlphabets(length):
    randomString = ''
    for i in range(length):
        randomString += alphabets[random.randint(0,51)]
    return randomString

def generateInt(length):
    return math.floor(random.random() * (10**length))

def generateRealNumber(prefix,precision):
    precision = '.'+str(precision)+'f'
    randomRealNumber = format(random.random() * (10**prefix),precision)
    return randomRealNumber

types = ['alphanumeric','alphabets','integer','realnumber']

#download the file if exist
@app.route('/download/<path:filename>')
def downloadFile(filename):
    try:
        return send_file(os.getcwd()+'/'+filename,as_attachment=True)
    except FileNotFoundError:
        return {'message':'file not found','error':404}
    finally:
        pass

#generate random values and stores in a file
@app.route('/generate')
def generateRandomInput():
    default_input()
    fileName = 'randomString_'+ str(round(time.time() * 1000)) + '.txt'
    
    with open(fileName,'a+') as f: 
        while True:
            index = int(random.random()*10) % len(types)
            generatedType=types[index]
            
            if generatedType == 'alphanumeric':
                length = random.randint(10, 25)
                result = generateAlphaNumeric(length) + ','
            elif generatedType == 'alphabets':
                length = random.randint(10, 25)
                result = generateAlphabets(length) + ','
            elif generatedType == 'integer':
                length = random.randint(5, 8)
                result = str(generateInt(length)) + ','
            else:
                length = random.randint(5, 8)
                precision = random.randint(2, 7)
                result = str(generateRealNumber(length,precision)) + ','
            fileSize = os.path.getsize(fileName)
            
            if (fileSize + len(result) <= 2 * 1000 * 1000):
                generatedInput[generatedType] +=1
                f.write(result)
            else:
                break
    generatedInput['fileName'] = fileName    
    return generatedInput

if __name__ =='__main__':
    app.run('127.0.0.1',5050)
            

        
    
