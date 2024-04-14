import requests
from urllib.request import urlretrieve
from tqdm import tqdm

def query(url):
    response = requests.get(url)
    return response.json()

output_folder = r'C:\Users\mcsgo\OneDrive\Documentos\Noise'

# dataset chosen has 5775 rows
n_rows = 5775
length = 100
sum = 0

while sum < n_rows:
    cant_request = True
    while cant_request:
        try:
            url = f'https://datasets-server.huggingface.co/rows?dataset=psiyou%2Fambient_noise_dataset&config=default&split=train&offset={sum}&length={length}'

            data = query(url)

            for ix, item in enumerate(data["rows"]):
                url = item['row']['audio'][0]['src']
                filename = output_folder + f'\{sum + ix+1}.wav'

                urlretrieve(url, filename)

            if n_rows - sum < length:
                sum += n_rows - sum
            else:
                sum += length
            cant_request = False
        except:
            length = int(length/2)
