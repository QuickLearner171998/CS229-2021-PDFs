import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "http://cs229.stanford.edu/syllabus-spring2021.html"

#If there is no such folder, the script will create one automatically
folder_location = "./cs229_2021_pdfs"
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")     
for link in soup.select("a[href$='.pdf']"):
    #Name the pdf files using the last portion of each link which are unique in this case
    subfolder = link['href'].split('/')[-2]
    subfolder_location = os.path.join(folder_location, subfolder)

    if not os.path.exists(subfolder_location):os.mkdir(subfolder_location)

    filename = os.path.join(subfolder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)