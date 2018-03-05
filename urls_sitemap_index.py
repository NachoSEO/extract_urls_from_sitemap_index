import requests
from bs4 import BeautifulSoup
import pandas as pd

def urls_sitemap_index(url_sitemap_index):
    sitemap = []
    urls = []
    xml = requests.get(url_sitemap_index)
    xml_parsed = BeautifulSoup(xml.content, "xml")
    sitemaps = xml_parsed.find_all("loc")
    for s in sitemaps:
        sitemap.append(s.text)
    for s in sitemap:
        uis = requests.get(s)
        uis_parsed = BeautifulSoup(uis.content, "xml")
        urls_loc1 = uis_parsed.find_all("loc")
        for u in urls_loc1:
            urls.append(u.text)
    return urls

urls = urls_sitemap_index("URL HERE") # poner la URL dentro de las comillas

df = pd.DataFrame({"urls":urls})
df.to_csv("urls-sitemap.csv", sep="\t", encoding="utf-8")
