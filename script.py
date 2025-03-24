import csv
import requests

API_URL = "http://127.0.0.1:8000"
LOGIN_ENDPOINT = f"{API_URL}/login"
USERS_ENDPOINT = f"{API_URL}/users"
CSV_FILE = "teste.csv"

LOGIN_DATA = {
    "username": "admin@example.com",
    "password": "senha123",
}

def get_jwt_token():
    response = requests.post(LOGIN_ENDPOINT, data=LOGIN_DATA)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Error while obtaining token:", response.json())
        return None

def send_user_data(user_data, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(USERS_ENDPOINT, json=user_data, headers=headers)

    if response.status_code == 200:
        print(f"{response.status_code} -> {response.json()}")
    else:
        print(f"{response.status_code} -> {response.json()}")

def read_csv_and_send_data():
    token = get_jwt_token()
    if not token:
        return

    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            send_user_data(row, token)

if __name__ == "__main__":
    read_csv_and_send_data()