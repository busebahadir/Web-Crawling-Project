# B9122 Homework 2 Repository

Author: Buse Bahadir

## Description

This repository contains Python scripts for web crawling and press release analysis. The scripts are designed to perform the following tasks:

1. **web_crawler.py**: This script is a basic web crawler implemented using Python. It utilizes the BeautifulSoup library to parse HTML content and urllib to make HTTP requests. The main purpose of this script is to crawl web pages starting from a seed URL (`https://www8.gsb.columbia.edu`) and extract child URLs found on these pages. The crawler follows child URLs that belong to the same domain as the seed URL and keeps track of URLs it has visited to prevent revisiting them. The maximum number of URLs to visit is set to 50.

2. **press_release_crawler.py**: This script is designed to crawl a specific website (`https://press.un.org/en`) and collect URLs of press releases that contain the word 'crisis.' It utilizes libraries such as BeautifulSoup, requests, pandas, tqdm, and time to perform this task. The script sends HTTP requests to the seed URL, extracts links from the page, and then checks each link for press releases containing the word 'crisis'.
