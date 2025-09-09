# 📊 Trader vs Sentiment Dashboard

This project analyzes **Bitcoin market sentiment (Fear/Greed Index)** and **historical trader data from Hyperliquid** to explore the relationship between market mood and trader behavior.  

It includes:
- A **Jupyter Notebook** for data analysis: `Trader_vs_Sentiment.ipynb`
- A **Streamlit Dashboard** (`dashboard_app.py`) for interactive visualization.  

---

## 🚀 Features
- ✅ Sentiment classification (Fear vs Greed)  
- ✅ Trader activity analysis (buy/sell size, execution prices, positions)  
- ✅ Interactive plots and dashboards (via Streamlit)  
- ✅ Ngrok/Colab support to run Streamlit apps in the cloud  

---

## 📂 Repository Structure
```
trader-sentiment-dashboard/
│── Trader_vs_Sentiment.ipynb   # Main analysis notebook
│── dashboard_app.py            # Streamlit dashboard script
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation
└── images/                     # (Optional) Screenshots, plots
```

---

## ⚙️ Installation
Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/trader-sentiment-dashboard.git
cd trader-sentiment-dashboard
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Notebook
Open in Jupyter/Colab:
```bash
jupyter notebook Trader_vs_Sentiment.ipynb
```

Or in Colab:
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/trader-sentiment-dashboard/blob/main/Trader_vs_Sentiment.ipynb)

---

## 🌐 Running the Dashboard
On local machine:
```bash
streamlit run dashboard_app.py
```

On Google Colab (with ngrok):
```python
from pyngrok import ngrok
!streamlit run dashboard_app.py --server.port 8501 &
public_url = ngrok.connect(8501)
print("Streamlit app running at:", public_url)
```

---

## 📸 Example Output
(Add a screenshot here once you upload an image, e.g.:)  

![Dashboard Screenshot](images/dashboard.png)

---

## 📜 License
This project is open-source under the **MIT License**.  
