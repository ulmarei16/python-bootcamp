#parsing - zczytywanie ze stronypi

from requests import get #<-- get to jest wywoływanie strony, post to jest wprowadzanie danych na stronie
from bs4 import BeautifulSoup

url ="https://helion.pl/search?qa=&serwisyall=&szukaj=python&wprzyg=&wsprzed=&wyczerp="
response = get(url)

#print(response)
#<Response [200]> to kod html, że wszystko wykanalo się dobrze

print(response.text) #<--drukuje to co jest pod pokaz kod strony
html_soup = BeautifulSoup(response.text, 'html.parser')
books = html_soup.find_all('div', class_="book-info") #zczytuje to co jest w tej klasie
print(len(books))
print(books[0])
for b in books:
    print(b.a.text) #<-- a jest tutaj kotwicą a to jest <a> z html


#zaznaczenie kilku wierszy srodkowym guzikiem lub (lewy alt +lewy klawisz) myski pozwala na wprowadzanie zmian we wszystkich wierasz w tym samym miejscu np na poczattku lub koncu