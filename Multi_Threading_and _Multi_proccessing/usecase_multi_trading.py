'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to 
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.
'''

"""
🕸️ What is Web Scraping?
✅ Web scraping means extracting data from websites automatically using a program.
Instead of copy-pasting information manually from a web page, you write code to fetch the page and extract the data you need.

🧠 How it works (step by step):
📡 Send a request to the website (like a browser does).
📃 Get back the HTML content of the page.
🔍 Parse the HTML and find the parts you care about (e.g., titles, prices, images).
📥 Save the extracted data (e.g., to a file or database).
"""

import threading
import requests
from bs4 import BeautifulSoup


urls=[
   'https://langchain-ai.github.io/langgraph/',
   'https://langchain-ai.github.io/langgraph/tutorials/langgraph-platform/local-server/',
   'https://langchain-ai.github.io/langgraph/concepts/why-langgraph/'
]

def fatch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")
    print(f" fatched - { len(soup.text)} characters from {url}")

threads=[] ## store all threads

for url in urls:
    thread=threading.Thread(target=fatch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all web scraping is done.")
