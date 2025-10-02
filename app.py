from flask import Flask, render_template, request
import os
import numpy as np
from carsales.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

# Home route
@app.route('/', methods=['GET'])
def homePage():
    return render_template("index.html")


# Trigger training from the browser
@app.route('/train/', methods=['GET'])
def training():
    os.system("python main.py")
    return "✅ Training successfully completed!"


# Prediction route
@app.route('/predict/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            # Collect input data from form
            make = str(request.form['make'])
            model = str(request.form['model'])
            year = int(request.form['year'])
            mileage = int(request.form['mileage'])
            engine_hp = int(request.form['engine_hp'])
            transmission = str(request.form['transmission'])
            fuel_type = str(request.form['fuel_type'])
            drivetrain = str(request.form['drivetrain'])
            body_type = str(request.form['body_type'])
            exterior_color = str(request.form['exterior_color'])
            interior_color = str(request.form['interior_color'])
            owner_count = int(request.form['owner_count'])
            accident_history = str(request.form['accident_history'])
            seller_type = str(request.form['seller_type'])
            condition = str(request.form['condition'])
            trim = str(request.form['trim'])
            vehicle_age = int(request.form['vehicle_age'])
            mileage_per_year = float(request.form['mileage_per_year'])
            brand_popularity = float(request.form['brand_popularity'])

            # Arrange inputs in order as per model
            data = [
                make, model, year, mileage, engine_hp, transmission, fuel_type,
                drivetrain, body_type, exterior_color, interior_color, owner_count,
                accident_history, seller_type, condition, trim, vehicle_age,
                mileage_per_year, brand_popularity
            ]

            # Reshape to (1, 19)
            final_input = np.array([data])

            # Run prediction pipeline
            obj = PredictionPipeline()
            prediction = obj.predict(final_input)

            return render_template('results.html', prediction=prediction)

        except Exception as e:
            print("❌ Exception occurred:", e)
            return "Something went wrong. Check your inputs or server logs."

    else:
        return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
