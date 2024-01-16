from flask import Flask,request,render_template

app=Flask(__name__)     #creating object of the class Flask

@app.route("/")
def home():
    return "Welcome to Home Page"

@app.route("/calculate",methods=['GET'])
def maths_operation():
    operator=request.json['operator']
    number1=request.json['number1']
    number2=request.json['number2']

    if operator=="add":
        return number1+number2
    elif operator=="multiply":
        return number1*number2
    elif operator=="divide":
        return number1/number2
    else:
        return number1-number2

if __name__=="__main__":
    app.run()