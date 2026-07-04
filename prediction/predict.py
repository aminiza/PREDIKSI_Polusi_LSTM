"""
=========================================================
Prediction Module
LSTM PM2.5 Prediction
=========================================================

Author  : Amin Izana
Project : Air Pollution Prediction
Model   : Stacked LSTM

=========================================================
"""

# =========================================================
# Import Library
# =========================================================

import os
import joblib
import numpy as np
import pandas as pd
import tensorflow as tf

from keras.models import load_model


# =========================================================
# Konfigurasi
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "Model")


MODEL_PATH = os.path.join(
    MODEL_DIR,
    "best_model.keras"
)

FEATURE_SCALER_PATH = os.path.join(
    MODEL_DIR,
    "feature_scaler.pkl"
)

TARGET_SCALER_PATH = os.path.join(
    MODEL_DIR,
    "target_scaler.pkl"
)

ENCODER_PATH = os.path.join(
    MODEL_DIR,
    "ordinal_encoder.pkl"
)

FEATURE_COLUMNS_PATH = os.path.join(
    MODEL_DIR,
    "feature_columns.pkl"
)

SEQUENCE_LENGTH = 24


# =========================================================
# Load Seluruh Object
# =========================================================

try:

    model = load_model(MODEL_PATH)

    feature_scaler = joblib.load(
        FEATURE_SCALER_PATH
    )

    target_scaler = joblib.load(
        TARGET_SCALER_PATH
    )

    encoder = joblib.load(
        ENCODER_PATH
    )

    feature_columns = joblib.load(
        FEATURE_COLUMNS_PATH
    )

    print("✓ Prediction Module berhasil dimuat.")

except Exception as e:

    raise RuntimeError(
        f"Gagal memuat model : {e}"
    )


# =========================================================
# Selected Feature
# (HARUS sama dengan training)
# =========================================================

selected_features = [

    "PM10 (µg/m³)",
    "NO2 (µg/m³)",
    "SO2 (µg/m³)",
    "CO (mg/m³)",
    "O3 (µg/m³)",

    "Temperature (°C)",
    "Humidity (%)",
    "Wind Speed (m/s)",
    "Pressure (hPa)",

    "Season",
    "City",
    "Weather Condition",

    "Hour_sin",
    "Hour_cos",

    "Month_sin",
    "Month_cos",

    "Day_sin",
    "Day_cos"
]

# =========================================================
# Validasi File CSV
# =========================================================

def validate_csv(df: pd.DataFrame):
    """
    Memastikan file CSV sesuai dengan kebutuhan model.
    """

    # Minimal harus memiliki 24 baris
    if len(df) != SEQUENCE_LENGTH:
        raise ValueError(
            f"CSV harus memiliki tepat {SEQUENCE_LENGTH} baris data."
        )

    # Kolom wajib sebelum feature engineering
    required_columns = [
        "PM10 (µg/m³)",
        "NO2 (µg/m³)",
        "SO2 (µg/m³)",
        "CO (mg/m³)",
        "O3 (µg/m³)",
        "Temperature (°C)",
        "Humidity (%)",
        "Wind Speed (m/s)",
        "Pressure (hPa)",
        "Season",
        "City",
        "Weather Condition",
        "Hour",
        "Month",
        "Day of Week"
    ]

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(
            f"Kolom berikut tidak ditemukan pada CSV: {missing}"
        )

    if df.isnull().sum().sum() > 0:
        raise ValueError(
            "CSV masih memiliki nilai kosong (NaN)."
        )

    return True

# =========================================================
# Cyclic Feature Engineering
# =========================================================

def create_cyclic_features(df: pd.DataFrame):

    df = df.copy()

    df["Hour_sin"] = np.sin(
        2 * np.pi * df["Hour"].astype(float) / 24
    )

    df["Hour_cos"] = np.cos(
        2 * np.pi * df["Hour"].astype(float) / 24
    )

    df["Month_sin"] = np.sin(
        2 * np.pi * df["Month"].astype(float) / 12
    )

    df["Month_cos"] = np.cos(
        2 * np.pi * df["Month"].astype(float) / 12
    )

    df["Day_sin"] = np.sin(
        2 * np.pi * df["Day of Week"].astype(float) / 7
    )

    df["Day_cos"] = np.cos(
        2 * np.pi * df["Day of Week"].astype(float) / 7
    )

    return df

# =========================================================
# Ordinal Encoding
# =========================================================

def encode_categorical(df: pd.DataFrame):

    df = df.copy()

    categorical_cols = [
        "Season",
        "City",
        "Weather Condition"
    ]

    df[categorical_cols] = encoder.transform(
        df[categorical_cols]
    )

    return df

# =========================================================
# Feature Selection
# =========================================================

def select_features(df: pd.DataFrame):

    return df[selected_features].copy()

# =========================================================
# Feature Selection
# =========================================================

def select_features(df: pd.DataFrame):

    return df[selected_features].copy()

# =========================================================
# Feature Scaling
# =========================================================

def scale_features(df: pd.DataFrame):

    scaled = feature_scaler.transform(df)

    return scaled

# =========================================================
# PM2.5 Category
# =========================================================

def classify_pm25(value):

    if value <= 50:
        return "Baik"

    elif value <= 100:
        return "Sedang"

    elif value <= 150:
        return "Tidak Sehat untuk Kelompok Sensitif"

    elif value <= 200:
        return "Tidak Sehat"

    elif value <= 300:
        return "Sangat Tidak Sehat"

    else:
        return "Berbahaya"

# =========================================================
# Create LSTM Sequence
# =========================================================

def create_sequence(data):

    data = np.asarray(data)

    return data.reshape(
        1,
        SEQUENCE_LENGTH,
        len(selected_features)
    )

# =========================================================
# Main Prediction Function
# =========================================================

def predict_from_csv(csv_path):
    """
    Melakukan prediksi PM2.5 dari file CSV.

    Parameters
    ----------
    csv_path : str
        Lokasi file CSV yang di-upload.

    Returns
    -------
    dict
        Hasil prediksi dalam format dictionary.
    """

    try:

        # =====================================================
        # Membaca CSV
        # =====================================================

        df = pd.read_csv(csv_path)

        # =====================================================
        # Validasi
        # =====================================================

        validate_csv(df)

        # =====================================================
        # Feature Engineering
        # =====================================================

        df = create_cyclic_features(df)

        # =====================================================
        # Encoding
        # =====================================================

        df = encode_categorical(df)

        # =====================================================
        # Feature Selection
        # =====================================================

        X = select_features(df)

        # =====================================================
        # Feature Scaling
        # =====================================================

        X_scaled = scale_features(X)

        # =====================================================
        # Create Sequence
        # =====================================================

        X_sequence = create_sequence(X_scaled)

        # =====================================================
        # Prediction
        # =====================================================

        prediction_scaled = model.predict(
            X_sequence,
            verbose=0
        )

        # =====================================================
        # Inverse Scaling
        # =====================================================

        prediction = target_scaler.inverse_transform(
            prediction_scaled
        )[0][0]

        prediction = float(prediction)

        # =====================================================
        # Category
        # =====================================================

        category = classify_pm25(prediction)

        # =====================================================
        # Return
        # =====================================================

        return {

            "status": "success",

            "prediction": round(
                prediction,
                2
            ),

            "category": category,

            "sequence": SEQUENCE_LENGTH,

            "rows": len(df)

        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)

        }

# =========================================================
# Standalone Test
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("      LSTM PM2.5 Prediction Module")
    print("=" * 60)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    upload_dir = os.path.join(BASE_DIR, "uploads")

    # Membuat folder uploads jika belum ada
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    csv_path = os.path.join(upload_dir, "sample.csv")

    if not os.path.exists(csv_path):

        print("\n[ERROR]")
        print("File berikut tidak ditemukan :")
        print(csv_path)

        print("\nSilakan letakkan file CSV contoh pada folder uploads/")
        print("dengan nama : sample.csv")

    else:

        print("\nMelakukan prediksi...\n")

        result = predict_from_csv(csv_path)

        print("=" * 60)

        if result["status"] == "success":

            print("STATUS      : SUCCESS")
            print(f"Prediction : {result['prediction']} µg/m³")
            print(f"Category   : {result['category']}")
            print(f"Rows       : {result['rows']}")
            print(f"Sequence   : {result['sequence']}")

        else:

            print("STATUS : ERROR")
            print(result["message"])

        print("=" * 60)