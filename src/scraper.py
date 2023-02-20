import requests
from bs4 import BeautifulSoup

def scrape(website_url):
    new_subjects = []
    response = requests.get(website_url)
    response.status_code  
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'html.parser')
   
    for sib in soup.find('h3').find_next_siblings():
        if sib.name == "h3":
            break
        else:
            for element in sib.find_all(attrs={'class': 'list-subjects'}):
                subject = element.find(attrs={'class': 'primary-subject'}).text
                new_subjects.append(subject)

    return new_subjects
