from collections import Counter

import bs4
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    domains = []
    #Under the hood, requests.get() creates a new Session object for each request made.
    r = requests.get(url) #<Response [200]>
    r.raise_for_status()
    soup = Soup(r.text, "html.parser") #<class 'bs4.BeautifulSoup'>
    for tr in soup.find("div", TARGET_DIV).find_all("tr"): #<class 'bs4.element.ResultSet'>
        domains.append(tr.find_all("td")[2].text) #[2]] contains the domain name, which gets appended
    
    return domains

#get_common_domains() 
#len(get_common_domains()) 100

def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
    ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()
    #to get the email domain and not the name, split it by @
    filtered = [email.split("@")[-1] for email in emails if email.split("@")[-1] not in common_domains]
    
    return Counter(filtered).most_common()


#get_most_common_domains(emails)