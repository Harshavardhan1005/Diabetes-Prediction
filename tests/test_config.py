import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service


input_data = {
    "incorrect_range":
    {"Pregnancies": 7897897,
    "Glucose": 555,
    "BloodPressure": 99,
    "SkinThickness": 99,
    "Insulin": 12,
    "BMI": 789,
    "DiabetesPedigreeFunction": 75,
    "Age": 2
    },


    "incorrect_col":
    {"Pregnancies": 1,
    "Glucose": 20,
    "Blood Pressure": 99,
    "Skin Thickness": 99,
    "Insulin": 12,
    "BMI": 52,
    "Diabetes Pedigree Function": 1,
    "Age": 22
    },
}


def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message

