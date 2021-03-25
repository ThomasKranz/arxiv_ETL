import requests
from bs4 import BeautifulSoup

def scrape(website_url, new_subjects):
    response = requests.get(website_url)  # ask for the content of the website
    response.status_code  # print status code
    response.raise_for_status()  # raise error if get was not successful
    soup = BeautifulSoup(response.text, 'html.parser')
    #target = soup.find('h3')
    #for sib in target.find_next_siblings():
    for sib in soup.find('h3').find_next_siblings():
        if sib.name == "h3":
            break
        else:
            for element in sib.find_all(attrs={'class': 'list-subjects'}):
                subject = element.find(attrs={'class': 'primary-subject'}).text
                new_subjects.append(subject)

