"""
==========================================================
MODUL 2B
Verifikasi Model Deployment
==========================================================
"""

import os
import joblib
import tensorflow as tf

from keras.models import load_model


print("=" * 60)
print("      VERIFIKASI MODEL DEPLOYMENT")
print("=" * 60)

MODEL_DIR = "Model"

# ----------------------------------------------------------
# Daftar file yang harus tersedia
# ----------------------------------------------------------

required_files = {
    "Model LSTM": "best_model.keras",
    "Feature Scaler": "feature_scaler.pkl",
    "Target Scaler": "target_scaler.pkl",
    "Ordinal Encoder": "ordinal_encoder.pkl",
    "Feature Columns": "feature_columns.pkl"
}

loaded_objects = {}

print("\n[1] Mengecek keberadaan file...\n")

for name, filename in required_files.items():

    path = os.path.join(MODEL_DIR, filename)

    if os.path.exists(path):
        print(f"✓ {filename}")
    else:
        raise FileNotFoundError(f"{filename} tidak ditemukan.")


print("\n")
print("=" * 60)
print("[2] Memuat seluruh object...")
print("=" * 60)

# ----------------------------------------------------------
# Load Model
# ----------------------------------------------------------

loaded_objects["model"] = load_model(
    os.path.join(MODEL_DIR, "best_model.keras")
)

print("✓ Model berhasil dimuat")

# ----------------------------------------------------------
# Load Scaler
# ----------------------------------------------------------

loaded_objects["feature_scaler"] = joblib.load(
    os.path.join(MODEL_DIR, "feature_scaler.pkl")
)

print("✓ Feature Scaler berhasil dimuat")

loaded_objects["target_scaler"] = joblib.load(
    os.path.join(MODEL_DIR, "target_scaler.pkl")
)

print("✓ Target Scaler berhasil dimuat")

# ----------------------------------------------------------
# Load Encoder
# ----------------------------------------------------------

loaded_objects["encoder"] = joblib.load(
    os.path.join(MODEL_DIR, "ordinal_encoder.pkl")
)

print("✓ Ordinal Encoder berhasil dimuat")

# ----------------------------------------------------------
# Load Feature
# ----------------------------------------------------------

loaded_objects["feature_columns"] = joblib.load(
    os.path.join(MODEL_DIR, "feature_columns.pkl")
)

print("✓ Feature Columns berhasil dimuat")


print("\n")
print("=" * 60)
print("[3] Informasi Model")
print("=" * 60)

print(f"Jumlah Feature : {len(loaded_objects['feature_columns'])}")

print("\nDaftar Feature :\n")

for i, feature in enumerate(loaded_objects["feature_columns"], start=1):
    print(f"{i:02d}. {feature}")


print("\n")
print("=" * 60)
print("HASIL VERIFIKASI")
print("=" * 60)

print("✓ Semua file berhasil dimuat.")
print("✓ Tidak ada file yang rusak.")
print("✓ Model siap digunakan untuk Prediction Engine.")
print("✓ Model siap diintegrasikan dengan Flask API.")

print("=" * 60)