import pickle
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict')
def iris():
    return render_template('predict.html')
@app.route('/klasifikasi',methods=['POST','GET'])
def hasil():
    if request.method=='POST':
        input = request.form
        a = float(input['a'])
        b = float(input['b'])
        c = float(input['c'])
        d = float(input['d'])
        e = float(input['e'])
        f = float(input['f'])
        g = float(input['g'])
        h = float(input['h'])
        i = float(input['i'])
        pred = Model.predict([[a,b,c,d,e,f,g,h,i]])[0]
        return render_template('hasil.html',data=input,prediksi=pred)

if __name__ == '__main__':
    with open('ModelSatisfied','rb') as model:
        Model = pickle.load(model)
    app.run(debug=True)