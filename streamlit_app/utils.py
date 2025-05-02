# 🔧 utils.py – Helper Functions for Streamlit App

import pandas as pd
import numpy as np
import os
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error
from math import sqrt

# 📥 Load LSTM/GRU model

def load_keras_model(ticker, model_type):
    path = f"models/{model_type.lower()}_{ticker}.h5"
    if os.path.exists(path):
        return load_model(path)
    else:
        raise FileNotFoundError(f"Model not found: {path}")

# 📄 Load Prophet forecast CSV

def load_prophet_forecast(ticker):
    path = f"models/prophet_{ticker}_reduced.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        return df
    else:
        raise FileNotFoundError(f"Prophet CSV not found: {path}")

# 📊 Compute RMSE

def compute_rmse(y_true, y_pred):
    return round(sqrt(mean_squared_error(y_true, y_pred)), 4)

# 📈 Load actual vs predicted from npz

def load_npz_predictions(ticker):
    path = f"preprocessed/{ticker}_processed.npz"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Preprocessed NPZ not found for {ticker}")

    data = np.load(path)
    X_test = data['X_test']
    y_test = data['y_test']
    min_ = data['scaler_min_']
    max_ = data['scaler_max_']

    def rescale(y):
        return y * (max_ - min_) + min_

    y_test_rescaled = rescale(y_test.reshape(-1, 1))
    return X_test, y_test_rescaled
