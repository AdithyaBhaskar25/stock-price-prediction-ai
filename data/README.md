# 📁 `data/` – Dataset Reference

This folder serves as a reference to the dataset used in the project:

> **🎯 Cracking the Market Code: AI-Driven Stock Price Prediction using Time Series Analysis**

---

## 🔗 Full Dataset (Hosted on Kaggle)

The full dataset is compressed into a single archive and hosted on Kaggle to ensure fast and stable access.

📦 **[Download on Kaggle →](https://www.kaggle.com/datasets/adithyabhaskar2511/stock-market-analysis)**

### 📥 Download via Colab or CLI:

```bash
!kaggle datasets download -d adithyabhaskar/stock-data-split --unzip
```
# 📂 Dataset Structure
```After extraction, the dataset has the following layout:```

```
data/
├── static_raw/                  # Original raw datasets from Kaggle & Yahoo Finance
│   ├── nifty50/
│   ├── nifty100_5min/
│   └── financial_analysis/
│
├── processed/
│   ├── static/                  # Cleaned historical stock data (static)
│   ├── live/                    # yFinance-based live data
│   └── enriched/                # Enriched with indicators (SMA, EMA, RSI, MACD)```
```
Each CSV file includes columns like:

Date, Open, High, Low, Close, Volume

Additional features like SMA_20, EMA_50, RSI, etc.

## ⚠️ File Size Notice
Note: This GitHub folder does not include the full dataset due to size limitations.

Only sample files (or references) are included.
Please use the Kaggle-hosted ZIP archive for full access.

## 💡 Use Cases
This dataset is prepared and enriched to support:

✅ AI-driven stock price prediction (LSTM, GRU, Prophet)

✅ Trend classification (bullish/bearish)

✅ Real-time + historical analysis

✅ Feature engineering for financial time series

✅ Streamlit-powered dashboard integration

## 👥 Credits
This dataset is compiled and maintained by the team at Tagore Engineering College:

Name	Reg. No.	Responsibility
Adithya B	412723104003	Full-stack dev & integration
Hemnath S	412723104040	Model evaluation
Harish Kumar K	412723104037	Report writing & presentation
Joshua D	412723104051	Data collection & structuring
