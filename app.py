from flask import Flask , render_template, request
from datetime import datetime, timedelta
import pickle

app = Flask(__name__)

with open("./model/hpc.pkl",'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html',predictionVal="")


@app.route('/predict',methods=['POST'])
def predict():

    input_date_str = request.form['date']
    input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
    base_date = datetime(1904, 9, 1)
    numerical_date_value = (input_date - base_date).days

    date=numerical_date_value

    bedroom =request.form['bedroom']

    bathroom=request.form['bathroom']

    livingArea=request.form['livingArea']

    basement=request.form['basement']
    
    lot=request.form['lotArea']

    floor=request.form['floor']

    waterFront=request.form['waterFront']

    views=request.form['views']

    condtion=request.form['condition']

    grade=request.form['grade']

    builtYear=request.form['builtYear']

    renovYear=request.form['renovYear']

    postal=request.form['postalCode']

    renlivarea=request.form['renLivingArea']

    renlotArea=request.form['renLotArea']

    school=request.form['schools']

    airpot=request.form['airport']

    total_area= livingArea+basement

    # prediction=model.predict([[date,bedroom,bathroom,total_area,lot,floor,waterFront,views,condtion,grade,livingArea,basement,builtYear,renovYear,postal,renlivarea,renlotArea,school,airpot]])
    prediction=model.predict([[43467,5,1,1000,5000,2,1,1,4,7,500,500,2010,2023,574237,500,1500,5,10]])
    predictionVal = "The price of house is $ " + str(prediction[0])

    return render_template('index.html',predictionValue=predictionVal)

if __name__ == '__main__':
    app.run(debug=True)