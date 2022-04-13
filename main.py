import requests
from bs4 import BeautifulSoup


resp = requests.get('https://www.tgju.org/profile/price_dollar_rl')

soup = BeautifulSoup(resp.text, 'lxml')
price = soup.find('td' , class_ = "text-left" ).text


user_input = int(input('Enter your money: '))

var = price.split(',')[0]

result = float(user_input / int(var) * 1000) / 100000
final_re = round(result , 2)

print(f'dollar price is: {price} and with your money, you can have {final_re} dollars')
