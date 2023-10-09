import os
import requests
import logging
import time

# Kiểm tra và tạo thư mục 'log' nếu nó không tồn tại
if not os.path.exists('log'):
    os.makedirs('log')

logging.basicConfig(level=logging.INFO, handlers=[
    logging.FileHandler("log/download.log"),
    logging.StreamHandler()
])
def download_file(url, filename):
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(filename, 'wb') as file:
                file.write(response.content)
            logging.info(f'Successfully downloaded {filename}')
            return True
        except requests.HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            logging.error(f'An error occurred: {err}')
        time.sleep((2 ** (attempt + 1)) * 60)
    logging.error(f'Failed to download {url} after 3 attempts.')
    return False

def downloads(urls):
    recovery_list = set()
    for url in urls:
        file_id = url.split('/')[-2]
        filename = f'{file_id}_{url.split("/")[-1].replace("/", "_")}'
        if not download_file(url, filename):
            recovery_list.add(url)
    return recovery_list


