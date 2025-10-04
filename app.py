# from flask import Flask, render_template, request
# import os
# import numpy as np
# from carsales.pipeline.prediction import PredictionPipeline

# app = Flask(__name__)

# # Home route
# @app.route('/', methods=['GET'])
# def homePage():
#     return render_template("index.html")


# # Trigger training from the browser
# @app.route('/train/', methods=['GET'])
# def training():
#     os.system("python main.py")
#     return "✅ Training successfully completed!"


# # Prediction route
# @app.route('/predict', methods=['POST', 'GET'])
# def predict():
#     if request.method == 'POST':
#         try:
#             # Collect input data from form
#             make = str(request.form['make'])
#             model = str(request.form['model'])
#             year = int(request.form['year'])
#             mileage = int(request.form['mileage'])
#             engine_hp = int(request.form['engine_hp'])
#             transmission = str(request.form['transmission'])
#             fuel_type = str(request.form['fuel_type'])
#             drivetrain = str(request.form['drivetrain'])
#             body_type = str(request.form['body_type'])
#             exterior_color = str(request.form['exterior_color'])
#             interior_color = str(request.form['interior_color'])
#             owner_count = int(request.form['owner_count'])
#             accident_history = str(request.form['accident_history'])
#             seller_type = str(request.form['seller_type'])
#             condition = str(request.form['condition'])
#             trim = str(request.form['trim'])
#             vehicle_age = int(request.form['vehicle_age'])
#             mileage_per_year = float(request.form['mileage_per_year'])
#             brand_popularity = float(request.form['brand_popularity'])

#             # Arrange inputs in order as per model
#             data = [
#                 make, model, year, mileage, engine_hp, transmission, fuel_type,
#                 drivetrain, body_type, exterior_color, interior_color, owner_count,
#                 accident_history, seller_type, condition, trim, vehicle_age,
#                 mileage_per_year, brand_popularity
#             ]

#             # Reshape to (1, 19)
#             final_input = np.array([data])

#             # Run prediction pipeline
#             obj = PredictionPipeline()
#             prediction = obj.predict(final_input)

#             return render_template('results.html', prediction=prediction)

#         except Exception as e:
#             print("❌ Exception occurred:", e)
#             return "Something went wrong. Check your inputs or server logs."

#     else:
#         return render_template('index.html')


# # Run the app
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=8080, debug=True)

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
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            # Collect input data from form with type conversions
            make = request.form['make']
            model = request.form['model']
            year = int(request.form['year'])
            mileage = int(request.form['mileage'])
            engine_hp = int(request.form['engine_hp'])
            transmission = request.form['transmission']
            fuel_type = request.form['fuel_type']
            drivetrain = request.form['drivetrain']
            body_type = request.form['body_type']
            exterior_color = request.form['exterior_color']
            interior_color = request.form['interior_color']
            owner_count = int(request.form['owner_count'])
            accident_history = request.form.get('accident_history', '').strip()  # handle empty gracefully
            seller_type = request.form['seller_type']
            condition = request.form['condition']
            trim = request.form['trim']
            vehicle_age = int(request.form['vehicle_age'])
            mileage_per_year = float(request.form['mileage_per_year'])
            brand_popularity = float(request.form['brand_popularity'])

            # Debug: print all inputs to server log
            print("Received inputs:")
            print({
                "make": make, "model": model, "year": year, "mileage": mileage,
                "engine_hp": engine_hp, "transmission": transmission, "fuel_type": fuel_type,
                "drivetrain": drivetrain, "body_type": body_type, "exterior_color": exterior_color,
                "interior_color": interior_color, "owner_count": owner_count,
                "accident_history": accident_history, "seller_type": seller_type,
                "condition": condition, "trim": trim, "vehicle_age": vehicle_age,
                "mileage_per_year": mileage_per_year, "brand_popularity": brand_popularity
            })

            # NOTE: Your PredictionPipeline might expect features in a certain order and format,
            # including possible encoding for categorical variables.
            # Adjust this list accordingly to match what your model expects.

            data = [
                make, model, year, mileage, engine_hp, transmission, fuel_type,
                drivetrain, body_type, exterior_color, interior_color, owner_count,
                accident_history, seller_type, condition, trim, vehicle_age,
                mileage_per_year, brand_popularity
            ]

            # Convert to numpy array with shape (1, n_features)
            final_input = np.array([data])

            # Run prediction
            pipeline = PredictionPipeline()
            prediction = pipeline.predict(final_input)

            return render_template('results.html', prediction=prediction)

        except Exception as e:
            print("❌ Exception occurred:", e)
            return "Something went wrong. Check your inputs or server logs."

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

