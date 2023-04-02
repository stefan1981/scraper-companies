from bs4 import BeautifulSoup
import os

def get_value(field_name):
    ret_val = ''
    for res in soup.find_all('div', {'class' : field_name}):
      tmp = res.find('a')
      if tmp:
          ret_val = [tmp.contents[0], tmp['href']]
      else:
          ret_val = process_number(res.find('div', {'class' : 'field--item'}).contents[0])

    return ret_val


def process_number(val):
    if 'Million USD' in val:
        tmp = val.replace(" Million USD", "").replace(",", "").replace(".", "")
        return tmp+"000000"
    if 'Billion USD' in val:
        tmp = val.replace(" Billion USD", "").replace(",", "").replace(".", "")
        return tmp+"000000"
    return val.replace(",", "")


def get_link(name, index=1):
    val = get_value(name)
    if val:
      return val[index]
    else:
      return ''


def show_csv():
    arr = []
    arr.append(get_link('field--name-node-title', 0))
    arr.append(get_value('field--name-field-world-rank-jan072022'))
    arr.append(get_value('field--name-field-market-value-jan072022'))
    arr.append(get_value('field--name-field-revenue-in-usd'))
    arr.append(get_value('field--name-field-net-income-in-usd'))
    arr.append(get_link('field--name-field-city', 0))
    arr.append(get_link('field--name-field-headquarters-of-company', 0))
    arr.append(get_link('field--name-field-stock-exchange-lc', 0))
    arr.append(get_value('field--name-field-listed-year'))
    arr.append(get_value('field--name-field-founded-year'))
    arr.append(get_value('field--name-field-employee-count'))
    arr.append(get_link('field--name-field-ceo', 0))
    arr.append(get_link('field--name-field-yahoo', 1))
    arr.append(get_link('field--name-field-wikipedia', 1))
    arr.append(get_link('field--name-field-twitter', 1))
    arr.append(get_link('field--name-field-facebook', 1))
    arr.append(get_link('field--name-field-company-website', 1))

    line = '"' + '";"'.join(arr) + '"'
    return line


def show_stats():
    print('Company: ', get_value('field--name-node-title'))
    print('World Rank: ', get_value('field--name-field-world-rank-jan072022'))
    print('Market Value Jan 07 2022: ', get_value('field--name-field-market-value-jan072022'))

    print('Revenue in USD: ', get_value('field--name-field-revenue-in-usd'))
    print('Net income in USD: ', get_value('field--name-field-net-income-in-usd'))
    print('Headquarter region: ', get_value('field--name-field-city'))
    print('Headquarter country: ', get_value('field--name-field-headquarters-of-company'))
    print('Stock-Exchange: ', get_value('field--name-field-stock-exchange-lc'))
    print('IPO: ', get_value('field--name-field-listed-year'))
    print('Founded: ', get_value('field--name-field-founded-year'))

    print('Employees: ', get_value('field--name-field-employee-count'))
    print('CEO: ', get_value('field--name-field-ceo'))
    print('Yahoo: ', get_value('field--name-field-yahoo'))
    print('Wikipedia: ', get_value('field--name-field-wikipedia'))
    print('Twitter: ', get_value('field--name-field-twitter'))
    print('Facebook: ', get_value('field--name-field-facebook'))
    print('Website: ', get_value('field--name-field-company-website'))

# create list of company files
files=[]
dir_path='company'
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        files.append(path)

#open text file
text_file = open("companies.csv", "w")
head = '"name";"rank";"market_cap";"revenue";"net_income";"hq_city";"hq_country";"stock_exchange";"ipo";"founded";"employees";"ceo";"yahoo";"wikipedia";"twitter";"facebook";"website"' + "\n"
text_file.write(head)

for my_file in files:
    with open("company/" + my_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        line = show_csv()
        text_file.write(line+"\n")
        print(line)


text_file.close()


