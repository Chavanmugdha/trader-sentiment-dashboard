import streamlit as st

st.set_page_config(page_title="Trader vs Sentiment Dashboard", layout="wide")

st.title("📊 Trader vs Sentiment Dashboard")
st.write("This is a placeholder Streamlit app. Extend it with charts and analysis.")

# Example chart
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Sentiment": ["Fear", "Greed", "Fear", "Greed"],
    "Value": np.random.randint(10, 100, 4)
})

st.bar_chart(df.set_index("Sentiment"))
