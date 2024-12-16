import requests

# Base URL dari API
BASE_URL = "http://localhost:5000/data"

# CREATE (POST)
def store_to_database(humidity, temp):
    payload = {"humidity": humidity, "temp": temp}
    
    try:
        # Mengirim request POST
        response = requests.post(BASE_URL, json=payload)
        
        # Debugging response
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Text: {response.text}")

        # Menangani response
        if response.status_code == 200:
            print("Item Created:", response.json())
        else:
            print("Failed to Create Item:", response.text)
    
    except requests.exceptions.RequestException as e:
        print("Error occurred while making the request:", e)

# Panggil fungsi untuk membuat item baru
store_to_database(50, 100)
