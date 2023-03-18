import concurrent.futures
import requests
import threading
import time

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content),url))


def download_all(sites):
    # 创建线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one,sites)


def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts', 'https://en.wikipedia.org/wiki/Portal:History', 'https://en.wikipedia.org/wiki/Portal:Society',
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites),end_time - start_time))


if __name__ == '__main__':
    main()