import requests
import datetime
import os

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_END_POINT = os.environ["SHEETY_END_POINT"] #END POINT OF SHEETY
TOKEN = os.environ["TOKEN"]
print(API_ID)
print(API_KEY)
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise" #END POINT OF NUTRITIONIX

sheety_header = {
    "Authorization": TOKEN
}
header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
query = input("Enter your workout")
parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": "62",
    "height_cm": "162",
    "age": "23",
}

Day = datetime.datetime.now().date().strftime("%x")
Time = datetime.datetime.now().time().strftime("%X")

response = requests.post(url=END_POINT, json=parameters, headers=header)
result = response.json()
print(result)
for exercise in result["exercises"]:
    let_body = {
        "sheet1": {
            "date": Day,
            "time": Time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=SHEETY_END_POINT, json=let_body, headers= sheety_header)
    print(sheety_response.text)
