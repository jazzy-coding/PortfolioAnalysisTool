"""Module for yfinance market data ingestion."""
import datetime as dt
import polars as pl
import yfinance as yf

def get_market_data(tickers: list[str], start_date: dt.date, end_date: dt.date) -> pl.DataFrame:
    """Function to get market data from the yfinance API."""
    return pl.DataFrame()



