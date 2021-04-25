import requests

# url = http://api.github.com/    
# response = requests.get(url)

# if response.status_code == 200:
#     print("success!")
# elif response.status_code == 404:
#         print("not found!")

# from requests.exceptions import HTTPError

# for url in ["http://api.github.com/","http://api.github.com/invalid"]:  #http://api.github.com ROOT REST API root end point
#     try:
#         response = requests.get(url)

#         #if response was successful no status will be raised
#         response.raise_for_status()
#     except HTTPError as http_err:
#         raise SystemExit(http_err)
#     except Exception as err:
#         print(f'other error {err} occurred')
#     else:
#         print('Success!')
   
IPINFO_URL = 'http://ipinfo.io/{ip}/json'
def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    try:
        response = requests.get(IPINFO_URL, ip_address)
        response.raise_for_status()
        return response.json().get('country')
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

