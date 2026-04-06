"""Module for yfinance market data ingestion."""

import datetime as dt
import pandas as pd
import yfinance as yf


def get_market_data(
    tickers: list[str], start_date: dt.date, end_date: dt.date
) -> pd.DataFrame | None:
    """Function to get market data from the yfinance API."""
    df = yf.download(tickers=tickers, start=start_date, end=end_date)
    return df
