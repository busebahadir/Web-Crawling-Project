#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
get_ipython().system('pip install tqdm')
from tqdm.notebook import tqdm
import time 
import pandas as pd


# In[15]:


def is_pr_and_crisis(seed_url):
    
    headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
    
    print("Fetching seed URL:", seed_url)
    response = requests.get(seed_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    link_elements = soup.find_all('a', href=True)
    urls = []

    for link_element in link_elements:
        url = link_element['href']
        absolute_link_url = urljoin(seed_url, url)
        if absolute_link_url.startswith(seed_url) :
            urls.append(absolute_link_url)
    
    urls = pd.Series(urls).drop_duplicates().tolist()

    print(f"Found {len(urls)} links in seed URL.")

    press_releases = []
    not_press_release = []

    print("Checking links for press releases with 'crisis'...")
    for i in urls:
        response = requests.get(i, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        tag = soup.find('a', {'href': '/en/press-release', 'hreflang': 'en'})
        if tag and 'crisis' in response.text.lower():
            press_releases.append(i)
        else:
            not_press_release.append(i)

    press_releases = pd.Series(press_releases).drop_duplicates().tolist()
    not_press_release = pd.Series(not_press_release).drop_duplicates().tolist()

    print(f"Found {len(press_releases)} press releases with 'crisis' from the initial links.")

    new_links = []
    press_links = []
    if len(press_releases) >= 10:
        print("Enough press releases found.")
        print(press_releases)
    else:
        print("Not enough press releases found. Searching for more links...")
        for url in urls:
            if "press-release" in url:
                press_links.append(url)
        for link in press_links:
            base_url = link + "?page={}"
            for page in tqdm(range(2)):
                webpage = requests.get(base_url.format(page), headers=headers)
                print(f"Fetching page {page+1} for URL: {link}")
                soup = BeautifulSoup(webpage.content, "html.parser")
                link_elements = soup.find_all('a', href = True)
                for link_element in link_elements:
                    url = link_element['href']
                    absolute_link_url = urljoin(seed_url, url)
                    new_links.append(absolute_link_url)

    new_links = pd.Series(new_links).drop_duplicates().tolist()

    print(f"Found {len(new_links)} new links.")

    press_releases = []
    not_press_release = []

    print("Checking new links for press releases with 'crisis'...")
    for link in new_links:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        tag = soup.find('a', {'href': '/en/press-release', 'hreflang': 'en'})
        if tag and 'crisis' in response.text.lower():
            press_releases.append(link)
        else:
            not_press_release.append(link)

    press_releases = pd.Series(press_releases).drop_duplicates().tolist()
    not_press_release = pd.Series(not_press_release).drop_duplicates().tolist()

    print(f"Found {len(press_releases)} press releases with 'crisis' from the new links.")
    if len(press_releases) >= 10:
        print("Enough press releases found.")
        print(press_releases)


# In[16]:


is_pr_and_crisis("https://press.un.org/en")


# In[ ]:




