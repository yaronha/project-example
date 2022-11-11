import src.data_prep


def test_data_prep():
    data, label = src.data_prep.breast_cancer_generator()
    print(data.info())
    assert data.shape[1] == 31
    assert label == "label"
