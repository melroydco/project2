from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',predictionVlaue="")


@app.route('/predict',methods=['POST'])
def predict():
    prediction =request.form['bedroom']
    return render_template('index.html',predictionValue=prediction)

if __name__ == '__main__':
    app.run(debug=True)