from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object 

@app.route('/') #decorator drfines the   
def getMethod1():  
    return "hello, this is our first flask website";  
  
 
@app.route('/home/<name>') #decorator drfines the   
def home(name):  
    return "hello, this is our first flask website        "+name;  
  
if __name__ =='__main__':  
    app.run(debug = True)  