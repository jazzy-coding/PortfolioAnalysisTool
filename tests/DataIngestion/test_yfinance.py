"""Unit tests for yfinance.py script"""

import datetime as dt
import pytest
from unittest.mock import patch
import pandas as pd

from src.DataIngestion.yfinance import get_market_data


def test_get_market_data():
    """Test 'get_market_data' function"""
    # arrange
    tickers = ["VUSA.L", "VUKG.L"]
    start_date = dt.date.today() - dt.timedelta(days=365)
    end_date = dt.date.today()
    mock_df = pd.DataFrame(
        {
            ("Close", "VUSA.L"): [100.0, 101.0],
            ("Close", "VUKG.L"): [200.0, 202.0],
        }
    )

    # act
    with patch(
        "src.DataIngestion.yfinance.yf.download", return_value=mock_df
    ) as mock_download:

        result = get_market_data(
            tickers=tickers, start_date=start_date, end_date=end_date
        )

    # assert
    mock_download.assert_called_once_with(
        tickers=tickers, start=start_date, end=end_date
    )

    assert result is mock_df


def test_get_market_data_no_tickers():
    """Test 'get_market_data' with no tickers."""
    # arrange
    tickers = []
    start_date = dt.date.today() - dt.timedelta(days=365)
    end_date = dt.date.today()

    # act and assert
    with patch(
        "src.DataIngestion.yfinance.yf.download", side_effect=ValueError
    ):
        with pytest.raises(ValueError, match="Tickers must not be empty."):
            get_market_data(tickers=tickers, start_date=start_date, end_date=end_date)


def test_get_market_data_invalid_dates():
    """Test 'get_market_data' function with invalid dates."""
    # arrange
    tickers = ['VUSA.L', 'VUKG.L']
    start_date = dt.date.today()
    end_date = dt.date.today() - dt.timedelta(days=365)

    # act and assert
    with patch(
        "src.DataIngestion.yfinance.yf.download", side_effect=ValueError
    ):
        with pytest.raises(ValueError, match="Start date must be before end date."):
            get_market_data(tickers=tickers, start_date=start_date, end_date=end_date)
