"""
==========================================================
Flask REST API
PM2.5 Prediction
==========================================================
"""

from flask import Flask
from flask import request
from flask import jsonify

import os

from predict import predict_from_csv


# ==========================================================
# Flask Configuration
# ==========================================================

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================================
# Home
# ==========================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "status": "success",

        "message": "PM2.5 Prediction API",

        "version": "1.0"

    })


# ==========================================================
# Prediction Endpoint
# ==========================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ----------------------------------------
        # cek file
        # ----------------------------------------

        if "file" not in request.files:

            return jsonify({

                "status": "error",

                "message": "File CSV tidak ditemukan."

            }), 400

        file = request.files["file"]

        if file.filename == "":

            return jsonify({

                "status": "error",

                "message": "Tidak ada file yang dipilih."

            }), 400


        # ----------------------------------------
        # hanya CSV
        # ----------------------------------------

        if not file.filename.lower().endswith(".csv"):

            return jsonify({

                "status": "error",

                "message": "File harus berformat CSV."

            }), 400


        # ----------------------------------------
        # simpan file
        # ----------------------------------------

        save_path = os.path.join(

            app.config["UPLOAD_FOLDER"],

            file.filename

        )

        file.save(save_path)


        # ----------------------------------------
        # prediction
        # ----------------------------------------

        result = predict_from_csv(save_path)

        if result["status"] == "error":

            return jsonify(result), 400

        return jsonify(result), 200

    except Exception as e:

        return jsonify({

            "status": "error",

            "message": str(e)

        }), 500


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )