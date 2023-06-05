from flask import Flask,request,jsonify,render_template

app=Flask(__name__)

#route
@app.route('/')
def new():
    return render_template('index.html')
@app.route('/aboutus')
def aboutus():
    return "we are evr's"

@app.route('/demo',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result=0
        if operation=='add':
            result=num1+num2
        elif operation=='sub':
            result=num1-num2
        elif operation=='mul':
            result=num1*num2
        elif operation=='div':
            result=num1/num2

        return f"the operation is {operation} and result is {result}"
@app.route('/operation',methods=['POST'])
def operation():
    if(request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0
        if operation=='add':
            result=num1+num2
        elif operation=='sub':
            result=num1-num2
        elif operation=='mul':
            result=num1*num2
        elif operation=='div':
            result=num1/num2

        return render_template('result.html',result=result)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)