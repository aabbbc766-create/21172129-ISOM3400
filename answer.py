import streamlit as st
import pandas as pd

st.set_page_config(page_title="Submission Template", layout="wide")

st.title("📝 Assignment Submission")

# ==========================================
# Task 1
# ==========================================
st.header("Task 1: Build a stock dashboard with sidebar controls")


# Starter code
ticker_info = pd.read_csv("https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/ticker_info.csv")

# extract S&P 100 tickers from ticker_info
ticker_list = list(ticker_info.Ticker.unique())

# Load the stock data
stock_data = pd.read_csv(
    "https://github.com/justinjiajia/datafiles/raw/refs/heads/main/stock_data_yf.csv", 
    parse_dates=['Date']
)

 
 

st.info("Write your Task 1 code below ...")

# --- STUDENT CODE AREA START ---
with st.sidebar:

    show_sector = st.checkbox("Show Market Cap by Sector", True)

    selected_tickers = st.multiselect(
        "Select Companies", 
        options=ticker_list,
        default=['TSLA', 'NVDA', 'AAPL']
    )

    selected_years = st.slider(
        "Select Year Range",
        min_value = 2020,
        max_value = 2025,
        value = (2024,2025)

    )

if show_sector：
    st.header("Market Cap by Sector")
    st.bar_chart(ticker_info, x = "Sector", y = "Market Cap (B)", color = "Ticker", horizontal = True, width = 720, height = 500)

if selected_tickers:

    chart_data = stock_data.query(f"Date <= '{selected_years[1]}-12-31' and Date >= '{selected_years[1]}-01-01}' and Ticker in ") 

    st.header (f"Stock Trend Analysis ({selected_years[0]} - {selected_years[1]})")

    st.subheader("Closing Price")
    st.line_chart(chart_data, x="Date", y = "Close", color="Ticker", width = 720, height = 500)

    st.subheader("Trading Volume")
    st.bar_chart(chart_data, x="Date", y = "Volume", color="Ticker", width = 720, height = 500)

else:
    st.error("Please select at least one stock")









# --- STUDENT CODE AREA ---

st.divider()

# ==========================================
# Task 2
# ==========================================

st.header("Task 2: Display a video based on user input")

st.info("Write your Task 2 code below ...")

# --- STUDENT CODE AREA START ---

 




# --- STUDENT CODE AREA END ---