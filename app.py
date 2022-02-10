from flask import Flask, render_template, request, jsonify
import os
from prediction_service import prediction


webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        try:
            if request.form:
                dict_req = dict(request.form)
                response = prediction.form_response(dict_req)
                print(response)
                return render_template("result.html", prediction=response)
            elif request.json:
                response = prediction.api_response(request.json)
                return jsonify(response)

        except Exception as e:
            error = {"error": e}

            return render_template("404.html", error=error)
    else:
        return render_template("index1.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)