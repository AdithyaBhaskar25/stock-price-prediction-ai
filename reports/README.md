# 📊 Stock Price Forecasting Using Deep Learning and Prophet

This project involves time series forecasting of stock prices using LSTM, GRU, and Prophet models. It covers all phases from data collection and preprocessing to model evaluation and deployment.

---

## 📁 Phase 1: Data Collection and Preprocessing

### ✅ Objective
To collect reliable historical stock price data and preprocess it for effective time series modeling.

### 📌 Actions Performed
- **Stock Selection**: TCS, INFY, ITC (NSE) and AAPL (NASDAQ).
- **Data Sources**: Collected using `yfinance` for each selected stock.
- **Preprocessing Tasks**:
  - Handled missing values.
  - Normalized and scaled data.
  - Stored final processed data in the `processed/` folder.

### 📂 Outputs
- Raw data in `raw/`
- Cleaned and scaled datasets in `processed/`

---

## 📁 Phase 2: Model Building and Training

### ✅ Objective
To build, train, and compare the performance of LSTM, GRU, and Prophet models on each stock.

### 🧠 Models Used
- Long Short-Term Memory (LSTM)
- Gated Recurrent Unit (GRU)
- Facebook Prophet (for classical time-series forecasting)

### ⚙️ Features
- Modular training via `notebook4`.
- Lightweight training with reduced epochs.
- Handles both univariate and time-stamped datasets.
- Robust error handling and logging.
- Visual comparison plots saved to `plots/`.
- Trained models stored in `models/`.

### 📌 Implementation Notes
- Prophet model was not successfully trained for AAPL due to data path issues.
- Datasets used for Prophet follow naming like: `prophet_{TICKER}_reduced.csv`.

---

## 📁 Phase 3: Web App & Deployment Pipeline

### ✅ Objective
To develop a fast and responsive web application for real-time model inference and comparison.

### 🛠️ App Features
- Built with `Flask`
- Real-time model loading and inference.
- User selects stock + model for forecast.
- Graceful error handling and fallback logic.
- Fast API response using pre-trained models.

### 📦 Files & Structure
- `app.py`: Main web application script.
- `utils.py`: Helper methods for prediction and plotting.

### 📈 Deployment Ready
- Models and plots are ready.
- Can be hosted locally or on platforms like Render or Heroku.
- Folder structure supports GitHub Pages for documentation hosting.

---

## 📂 Reports

Each phase includes detailed documentation and outcomes, compiled as PDFs:
- `Phase-1_Report.pdf`
- `Phase-2_Report.pdf`
- `Phase-3_Report.pdf`
- `Combined_Phase_Report.pdf` (Common version covering all three phases)

You can find these files in the `reports/` folder.

---

## 🗂️ Folder Structure Overview

```bash
├── data/               # data files
├── raw/               # Raw downloaded data
├── processed/          # Cleaned and preprocessed data
├── models/             # Trained models (LSTM, GRU, Prophet)
├── plots/              # Comparative visualizations
├── reports/            # PDF documentation
├── streamlit_app/      # Deployment files with streamlit
├── app.py              # Flask backend
├── utils.py            # Utility functions
├── requirements.txt    # Python package requirements
├── README.md           # Project overview
```
## 📸 Screenshots
# Preprocessed:
![preprocessed](https://github.com/user-attachments/assets/f8566906-d331-4446-852f-75f21807be33)

# Model Training:
![modeltraining](https://github.com/user-attachments/assets/c31437b0-2801-4bbc-b740-c1b4572cdb10)

# Preview CSV:
![previewCSV](https://github.com/user-attachments/assets/b8e0dea8-56a5-4f7c-8e7c-9659e73316c2)

# App Screenshot
![AppScreenshot](https://github.com/user-attachments/assets/4bc56a93-6e7a-45a5-aac2-1b85d1124dab)

**Thank You For Reading Until The End**
