import csv
import requests
import time

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def download_url(url):
    while True:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f'Error occurred: {e}, retrying...')
            time.sleep(0.5)

with open('data-postprocessed.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"', lineterminator='\n', strict=True)
    next(reader)  # skip header
    for id_, url, _, _ in reader:
        content = download_url(url)
        with open(f'output/{id_}.mp3', 'wb') as output_file:
            output_file.write(content)
            print(f'{id_}.mp3 done!')
        time.sleep(0.5)
