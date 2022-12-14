import pandas as pd

from src import data_prep


def test_data_preparation():
    df = get_data()
    train, test, label = data_prep.data_preparation(df, 0.2)

    assert label == "fare_amount"

    # check for expected types
    assert isinstance(train, pd.DataFrame)
    assert isinstance(test, pd.DataFrame)


def test_clean_df():
    df = get_data()
    df = data_prep.clean_df(df)

    # check if df contains unexpected values
    assert 0 in df["fare_amount"]
    assert 0 in df["pickup_longitude"]


def get_data():
    return pd.read_csv("./data/dataset.csv")
