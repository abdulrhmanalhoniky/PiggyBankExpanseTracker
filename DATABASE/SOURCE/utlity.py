import re
import requests
import os

TOKEN = "8742289878:AAHgb0dtkAYBMuvS8_h1oYsc6NZOe64P9eU"
MY_ID = "1484948828"
DB_NAME = "user_data.db"


def is_valid_email(email):
    # Simple yet effective regex for email validation
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Checking if email is not empty and matches regex
    if email and re.match(regex, email):
        return True
    return False


def upload_to_telegram():
    if not os.path.exists(DB_NAME):
        return False, "File not found!"

    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

    try:
        with open(DB_NAME, 'rb') as db_file:
            payload = {'chat_id': MY_ID, 'caption': 'uploaded database'}
            files = {'document': db_file}
            response = requests.post(url, data=payload, files=files)

        if response.status_code == 200:
            return True, "Upload successful!"
        else:
            return False, f"Failed to upload: {response.status_code}"
    except Exception as e:
        return False, f"Error: {str(e)}"
