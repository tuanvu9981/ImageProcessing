import requests
from bs4 import BeautifulSoup
import os

FOLDER_NAME = 'geeksImages'
	
def getdata(url):
	r = requests.get(url)
	return r.text
	
def generate_image_with_type(img_links: list, group_name: str, image_type: str):
    os.mkdir(FOLDER_NAME + "/" + group_name)
    for index, img_single_link in enumerate(img_links):
        img_data = requests.get(img_single_link).content
        img_name = str(index+1) + image_type
        with open(FOLDER_NAME + "/" + group_name + img_name, 'wb+') as file:
            file.write(img_data)

htmldata = getdata("https://www.geeksforgeeks.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
SVG_links = []
PNG_links = []
GIF_links = []

for item in soup.find_all('img'):
    img_src: str = item['src']
    print(img_src)
    # print(img_src[-4:]) 
    # [-4:-1] --> NOT INCLUDING LAST CHARACTER

    if (img_src.find('.svg', -4) != -1):
        SVG_links.append(img_src)

    if (img_src.find('.png', -4) != -1):
        PNG_links.append(img_src)

    if (img_src.find('.gif', -4) != -1):
        GIF_links.append(img_src)

os.mkdir(FOLDER_NAME)

generate_image_with_type(SVG_links, "SVG-Group/", ".svg")
generate_image_with_type(PNG_links, "PNG-Group/", ".png")
generate_image_with_type(GIF_links, "GIF-Group/", ".gif")

print("Completed without detecting any errors\n")