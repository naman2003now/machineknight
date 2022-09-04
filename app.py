from flask import Flask, request, jsonify
import json
app = Flask(__name__)  
 
@app.route('/')  
def home():  
    print(request.json)
    rent = 1000
    return str(rent)  
  
if __name__ =="__main__": 
    print("App is running") 
    app.run(debug = True)  