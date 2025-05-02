# 📊 Streamlit App – Stock Forecast Visualizer

import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
from utils import load_keras_model, load_prophet_forecast, load_npz_predictions, compute_rmse

# 📁 Config
st.set_page_config(page_title="Stock Forecast AI", layout="centered")

# 🧠 Title
st.title("📈 AI Stock Price Forecast")
st.markdown("Select a stock and model to view predictions")

# ✅ Supported tickers
available_tickers = ["TCS", "INFY", "ITC", "AAPL"]
models = ["LSTM", "GRU", "Prophet"]

# 🔽 Sidebar controls
with st.sidebar:
    selected_ticker = st.selectbox("Select Stock", available_tickers)
    selected_model = st.radio("Select Model", models)
    st.markdown("---")
    st.markdown("Built with ❤️ by Stock Predictors")

# 📊 Section: Comparison Plot
st.subheader(f"📊 Comparison Plot for {selected_ticker}")
plot_path = f"plots/{selected_ticker}_comparison.png"
if os.path.exists(plot_path):
    st.image(plot_path, use_container_width=True)
else:
    st.warning("⚠️ Plot not found for this stock.")

# 📄 Section: Forecast Preview
if selected_model == "Prophet":
    if selected_ticker == "AAPL":
        st.error("⚠️ Prophet model not available for AAPL due to file errors.")
    else:
        try:
            df = load_prophet_forecast(selected_ticker)
            st.subheader("📄 Forecast Table (Prophet)")
            st.dataframe(df.tail(20))
            st.download_button("Download Forecast CSV", df.to_csv(index=False), file_name=f"prophet_{selected_ticker}_forecast.csv")
        except Exception as e:
            st.error(f"Prophet CSV Load Error: {e}")




# ✅ Done
st.success("App Ready and Running!")
