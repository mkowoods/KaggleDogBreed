from tqdm import tqdm
import os
import requests
import config

#download

DATA_DIR = "data"
DATA_DIR_PATH = os.path.join(config.BASE_DIR, DATA_DIR)
BASE_URL = r"https://www.kaggle.com/c/dog-breed-identification/download/"
FILE = ['labels.csv.zip', 'sample_submission.csv.zip', 'test.zip', 'train.zip']


if not os.path.isdir(DATA_DIR_PATH): os.mkdir(DATA_DIR_PATH)

def download_file(url, filename):
    """
    Helper method handling downloading large files from `url` to `filename`. Returns a pointer to `filename`.
    """
    chunkSize = 1024
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        pbar = tqdm( unit="B", total=int( r.headers['Content-Length'] ) )
        for chunk in r.iter_content(chunk_size=chunkSize):
            if chunk: # filter out keep-alive new chunks
                pbar.update (len(chunk))
                f.write(chunk)
    return filename


def get_file_from_url(url, fname):
    """
    need to pass credentials to download from kaggle, but i'm using oauth
    :param url:
    :param fname:
    :return:
    """
    path = os.path.join(DATA_DIR_PATH, fname)
    if os.path.isfile(fname):
        print(f"File {fname} already exists @ {path}")
        return

    # Streaming, so we can iterate over the response.

    r = requests.get(url, stream=True)

    # Total size in bytes.
    total_size = int(r.headers.get('Content-Length', 0));
    print(total_size)
    with open(path, 'wb') as f:
         for data in r.iter_content(32 * 1024):
             f.write(data)



if __name__ == "__main__":
    url = BASE_URL+FILE[0]
    print(url)
    get_file_from_url(url, FILE[0])