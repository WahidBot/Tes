import requests
import time

# Ganti URL ini dengan URL aplikasi web yang berjalan di Codespace Anda
CODESPACE_APP_URL = 'https://<your-username>-<your-repository>-<random-id>.github.dev'

while True:
    try:
        response = requests.get(CODESPACE_APP_URL)
        if response.status_code == 200:
            print("Codespace is active")
        else:
            print(f"Received status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    # Tunggu 5 menit (300 detik) sebelum mengirimkan request berikutnya
    time.sleep(300)
