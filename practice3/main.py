from bs4 import BeautifulSoup as bs
import requests as req
import re

resp = req.get("https://opt-opt-opt.ru/catalog/zimnyaya_obuv_2/")
print("STATUS CODE: ", resp.status_code)
soup = bs(resp.text, 'html.parser')
allPriceList = soup.findAll("div", class_="bx_catalog_item double")
priceLists = []
nameList = []
allCostList = []

pattern1 = re.compile('\s\d\d;')

allString = [{
    "articulate": str,
    "sizes": [],
    "cost": int,
    "mark": str
}]


for data in allPriceList:
    if data.find('div', class_="bx_price") is not None:
        priceLists.append(" ".join(data.text.split()))
    # if data.find('div', class_="bx_catalog_item_articul") is not None:
    #     nameList.append(" ".join(data.text.split()))

for pl in priceLists:
    number = [str(w) for w in pl.split() if w.isdigit()]
    # print(number)
    cost = 0
    if int(number[-2]) < 30:
        cost = number[-2] + number[-1]
    else:
        cost = number[-1]

    if int(number[0]) > 1000:
        number.pop(0)

    size = re.findall(pattern1, pl)
    size.append(number[0])
    # print("size after: ", size)
    findMarks = re.split(r'Размеры:', pl)[0].split(r'марка')[1]
    # print('indexMarka --> {0}'.format(findMarks))
    # print("{0} \n".format(pl.split()))
    allCostList.append(int(cost))
    allString.append(dict(articulate=pl.split()[1], sizes=size, cost=cost, mark=findMarks))

for data in allString:
    print("Артикул: {0}, Размеры: {1}, Марка: {2}, Цена: {3} руб."
          .format(data['articulate'], data['sizes'], data['mark'], data['cost']))

print("\nСамая дорогая обувь --------> {0} руб.".format(sorted(allCostList, reverse=True)[0]))
print("Самая дешёвая обувь --------> {0} руб.".format(sorted(allCostList, reverse=True)[-1]))
print("Общая стоимость товаров -------> {0} руб.".format(sum(allCostList)))
