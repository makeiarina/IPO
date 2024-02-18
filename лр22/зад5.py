import requests
from bs4 import BeautifulSoup
header={'user_agent':'safkpsfakpsafp'}
link = "https://browser-info.ru/"
response = requests.get(link, headers=header).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id="tool_padding")

# Check js
check_js = block.find('div', id ='javascript_check')
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'

# Check
check_flash = block.find('div', id ="flash version")
status_flash = check_flash.find_all('span')[1].text
result_flash=f'flash: {status_flash}'

# Check user-agent
check_user= block.find('div', id ="user_agent").text
print(result_js)
print(result_flash)
print(check_user)