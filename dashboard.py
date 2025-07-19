import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Live Stock Price Tracker")
st.title("📈 Live Stock Price Tracker")

ticker = st.text_input("Enter Ticker Symbol", "RELIANCE.NS")
threshold = st.number_input("Set Alert Threshold", value=3000.0)

if st.button("Track"):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", interval="1m")
    price = data['Close'].iloc[-1]
    st.metric(label=f"{ticker} Current Price", value=f"₹{price:.2f}")

    if price > threshold:
        st.error(f"🚨 Alert: {ticker} crossed ₹{threshold}!")