from flask import Flask,request,render_template,jsonify
import json 

app=Flask(__name__)     #creating object of the class Flask

@app.route("/")
def home():
    return "Welcome to Home Page"

@app.route("/calculate",methods=['GET'])
def maths_operation():
    operator=request.json["operator"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operator=="add":
        result= int(number1)+int(number2)
    elif operator=="multiply":
        result= int(number1)*int(number2)
    elif operator=="divide":
        result= int(number1)/int(number2)
    else:
        result= int(number1)-int(number2)
    
    return "The operation is {} and the result is {}".format(operator,result)

if __name__=="__main__":
    app.run()