"""Module for yfinance market data ingestion."""

import datetime as dt
import pandas as pd
import yfinance as yf


def get_market_data(
    tickers: list[str], start_date: dt.date, end_date: dt.date
) -> pd.DataFrame | None:
    """Function to get market data from the yfinance API."""
    # guard clauses
    if not tickers:
        raise ValueError("Tickers must not be empty.")
    if start_date >= end_date:
        raise ValueError("Start date must be before end date.")

    df = yf.download(tickers=tickers, start=start_date, end=end_date)
    return df
