from bs4 import BeautifulSoup
import csv
import re
import requests
from time import sleep

LOGIN_DATA = {
    'amember_login': '...',  # modify this!
    'amember_pass': '...',  # modify this!
}

assert LOGIN_DATA['amember_login'] != '...', 'You should set your username and password in the script!'

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36'})

course_response = session.post('https://www.persianpod101.com/sign-in', data=LOGIN_DATA)
assert course_response.ok

with open('url-list.txt', encoding='utf-8') as f:
    course_urls = [line.rstrip('\n') for line in f]

def process_url(url):
    match = re.fullmatch('^.+/audio/(.+)\.mp3$', url)
    assert match, f"but got {url}"
    return match[1].replace('/', '-').strip()

seen = set()

with open('data.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', lineterminator='\n', strict=True)
    writer.writerow(('id_', 'text', 'english_text', 'url'))
    for lesson_url in course_urls:
        print(f'Scraping {lesson_url}...')
        response = session.get(lesson_url)
        assert response.ok
        lesson_soup = BeautifulSoup(response.text, 'lxml')
        data = set()
        for node in lesson_soup.select('button[type="button"][data-text][data-english-text][data-url]'):
            text = node.get('data-text').strip()
            english_text = node.get('data-english-text').strip()
            url = node.get('data-url').strip()
            id_ = process_url(url)
            curr = id_, text, english_text, url
            if curr not in seen:
                writer.writerow(curr)
                data.add(curr)
                seen.add(curr)
        assert data, f'No data for {lesson_url}' + str(response) + response.text
        sleep(30)
