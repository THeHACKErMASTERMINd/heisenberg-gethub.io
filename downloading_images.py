import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
def download_images(url, folder_name="downloaded_images"):
    cnt=0
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    response = requests.get(url)
    if response.status_code != 200:
        return
    soup=BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all("img")
    for img in img_tags:
        cnt+=1
        img_url = img.get("src")
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        if img_url.lower().endswith(".svg"):
            continue
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join(folder_name,str(cnt)+'.jpg')
            with open(img_name, "wb") as img_file:
                img_file.write(img_data)
            print(f"Done: {img_url}")
        except Exception as e:
            print(f"EROR 404 in {img_url}. because of: {e}")
    print("Mission accomplished baby ")
url = input("Enter the URL of the website ☻ : ")
download_images(url)
