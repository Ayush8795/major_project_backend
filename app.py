from flask import Flask,render_template,redirect,jsonify,url_for

import predict

app= Flask(__name__)


@app.route('/',methods=['GET'])
def welcome():
    return render_template("index.html")


@app.route('/predict/<path>',methods=['GET'])
def predict(path):
    pred= predict.prediction(path)
    return render_template("index.html",prediction=pred)


if __name__=='__main__':
    app.run(host="0.0.0.0",port=8000)
