from bs4 import BeautifulSoup
import requests 
import csv


url = requests.get("https://www.census.gov/programs-surveys/popest.html").content
soup = BeautifulSoup(url, "html.parser")

empty = []
for url in soup.find_all('a', href=True):
    print(url['href'])
    empty.append(url['href'])
    
empty = set(empty)
with open("PythonProject.csv",'w') as csvfile:
    write = csv.writer(csvfile, delimiter = ' ')
    write.writerows(empty)