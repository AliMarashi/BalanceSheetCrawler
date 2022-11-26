# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# pip install selenium~=4.4.3
# pip install requests
# pip install bs4
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd
import os
import glob
from tqdm import tqdm
from persiantools import digits
import pickle
from sys import exit
# os.chdir(r'C:\Users\user\Downloads')

def opener():
    driver = webdriver.Chrome("C:/Users/user/chromedriver.exe")
    driver.get('https://www.codal.ir/ReportList.aspx?search')

    link1 = driver.find_element(By.CSS_SELECTOR,'#reportType')
    link1.click()
    link1.send_keys(Keys.ARROW_DOWN)
    link1.send_keys(Keys.ARROW_DOWN)
    link1.send_keys(Keys.ARROW_DOWN)
    link1.send_keys(Keys.ENTER)
    options.add_experimental_option("detach" , True)
    return (print(driver.title))

def fund_selector(Fund, sleep):
    print(FixedIncome.iloc[Fund , 0] , Fund)
    driver.execute_script("window.scrollTo(0, 0);")
    link10 = driver.find_element(By.CSS_SELECTOR ,
                                 '#collapse-search-1 > div.card-body.p-1.py-2 > div:nth-child(1) > div > div > a')
    link10.click()

    search = driver.find_element(By.CSS_SELECTOR , "#txtSymbol").clear()
    search = driver.find_element(By.CSS_SELECTOR , "#txtSymbol")
    search.send_keys(FixedIncome.iloc[Fund , 0])
    time.sleep(sleep)
    search.send_keys(Keys.ENTER)
    return
def page_ditector():
    excelnum = driver.find_element(By.CSS_SELECTOR , '#divLetterFormList > div')
    excelnum = excelnum.text[-2 :]
    items = digits.fa_to_en(excelnum)
    items = pd.to_numeric(items)
    try :
        if items <= 21 :
            page = 1
        elif items <= 40 :
            page = 2
        elif items >= 41 :
            page = 3
    except :
        print('No Page')
    return page

def item_ditector(page,k):
    excelnum = driver.find_element(By.CSS_SELECTOR , '#divLetterFormList > div')
    excelnum = excelnum.text[-2 :]
    items = digits.fa_to_en(excelnum)
    items = pd.to_numeric(items)
    try :
        if k == 1 and page == 2:
            items = 20
        elif k == 1 and page == 3 :
            items = 20
        elif k == 2 and page == 2 :
            items = items - 20
        elif k == 2 and page == 3 :
            items = 20
        elif k == 3 and page == 3:
            items = items - 40
    except :
        items = 3
    items = items + 1
    return items

def next_page(k):
    if k == 1:
        pass
    elif k == 2:
        try:
            page = driver.find_element(By.CSS_SELECTOR ,
                                       '#divLetterFormList > nav > paging > ul > li:nth-child(4) > a')
            page.click()
        except:
            time.sleep(1)
            page = driver.find_element(By.CSS_SELECTOR ,
                                       '#divLetterFormList > nav > paging > ul > li:nth-child(6) > a')
            page.click()
    elif k == 3:
        try:
            page = driver.find_element(By.CSS_SELECTOR ,
                                       '#divLetterFormList > nav > paging > ul > li:nth-child(5) > a')
            page.click()
        except:
            time.sleep(1)
            page = driver.find_element(By.CSS_SELECTOR ,
                                       '#divLetterFormList > nav > paging > ul > li:nth-child(6) > a')
            page.click()
    return


def item_checker(i,StopChar):
    link = "#divLetterFormList > table > tbody > tr:nth-child({}) > td:nth-child(4) > span > a".format(i)
    link = driver.find_element(By.CSS_SELECTOR , link)
    link = link.text

    if StopChar in link:
        return True
    else:
        return False

def item_clicker(i):
    link = "#divLetterFormList > table > tbody > tr:nth-child({}) > td:nth-child(4) > span > a".format(
            i)
    # divLetterFormList > table > tbody > tr:nth-child(20) > td:nth-child(4) > span > a
    link = driver.find_element(By.CSS_SELECTOR , link)

    link1 = "#divLetterFormList > table > tbody > tr:nth-child({}) > td:nth-child(1) > a > strong".format(i)
    link1 = driver.find_element(By.CSS_SELECTOR , link1)
    name = link1.text

    fundlink = link.get_attribute('href')

    date = link.text[-24 :-14].replace("/" ,'')
    return (fundlink,date ,name)

def closer(sleep):
    time.sleep(sleep)
    link3 = driver.find_element(By.CSS_SELECTOR ,
                                '#ctl00_service > div.bootbox.modal.fade.show > div > div > div.modal-header > button')
    link3.click()
    return

def id_ditector() :
    IdList = ['ctl00_cphBody_ucSFinancialPosition_grdSFinancialPosition', '\\31 087','\\31 155','\\31 453','\\31 387','\\32 147','\\31 288']
    for i in IdList:
        try:
            link = "#{} > tbody > tr:nth-child(1) > td:nth-child(1)".format(i)
            link = driver.find_element(By.CSS_SELECTOR , link)
            k = i
        except:
            k = i
            pass
    return k

def link_maker(i,id,kind) :
    if kind == 1:
        link = "#{1} > tbody > tr:nth-child({0}) > td:nth-child(1) > span".format(
            i ,
            id)
        link = driver.find_element(By.CSS_SELECTOR , link)
        link1 = "#{1} > tbody > tr:nth-child({0}) > td:nth-child(2) > span".format(
            i ,
            id)
        link1 = driver.find_element(By.CSS_SELECTOR , link1)
    elif kind == 2:
        link = "#{1} > tbody > tr:nth-child({0}) > td:nth-child(5) > span".format(
            i ,
            id)
        link = driver.find_element(By.CSS_SELECTOR , link)
        link1 = "#{1} > tbody > tr:nth-child({0}) > td:nth-child(6) > span".format(
            i ,
            id)
        link1 = driver.find_element(By.CSS_SELECTOR , link1)
    return (link,link1)

def list_maker(id , kind) :
    l1 = []
    l2 = []
    for i in range(1,55):
        try:
            a = link_maker(i,id,kind)
            link = a[0]
            link1 = a[1]
            l1.append(link.text)
            l2.append(link1.text)
        except:
            break
    return (l1 , l2)

##

driver = webdriver.Chrome("C:/Users/user/chromedriver.exe")
##
Stock = pd.DataFrame()
Stocks = []
for q in tqdm(range(1,20)):
    Url = "https://codal.ir/ReportList.aspx?search&LetterType=6&AuditorRef=-1&PageNumber={}&Audited&NotAudited=false&IsNotAudited=false&Childs=false&Mains&Publisher=false&CompanyState=0&Length=12&Category=1&CompanyType=1&Consolidatable&NotConsolidatable=false"
    Url = Url.format(q)
    driver.get(Url)
    print("ali")
    Date = []
    Name = []
    LinkFund = []
    Pages = []
    time.sleep(10)
    Page = page_ditector()
    items = 21
    for i in tqdm(range(1 , items)) :
        ali = item_clicker(i)
        fundlink = ali[0]
        date = ali[1]
        name = ali[2]

        Name.append(name)
        Date.append(date)
        LinkFund.append(fundlink)
        # NameFund.append(FixedIncome.iloc[Fund , 0])


    StockLink = pd.DataFrame({
            'Name' : Name ,
            'Date' : Date ,
            'Link' : LinkFund
    })
    Stocks.append(StockLink)
df = pd.concat(Stocks)
df.to_excel('Stocks.xlsx' , index = False)
##
df1 = df
df1 = df1[~df1.Date.str.contains("Õ”«»—”?")].reset_index(drop = True)
##
l3=[]
l4=[]
StockLink = df1
j = 1
for j in tqdm(range(0, len(StockLink))):
    Url = StockLink['Link'][j] + "&sheetId=0"
    driver.get(Url)
    l1 = []
    l2 = []
    id = id_ditector()
    a = list_maker(id , 1)
    l1 = a[0]
    l2 = a[1]
    try:
        link_maker(1 , id , 2)
        a = list_maker(id , 2)
        l1.extend(a[0])
        l2.extend(a[1])
    except:
        l4.append(Url)
        pass
    Stock = pd.DataFrame({
            'Name' : l1 ,
            'number' : l2
    })
    a="‘‘‘"
    a
    # Stock.Name = Stock.Name.str.replace("\\u200c" , " ")
    Stock.rename(columns = {
            'number' : StockLink['Name'][j] + "-" + StockLink['Date'][j]
    } , inplace = True)
    Stock = Stock[Stock.Name != '']
    # Stock = Stock.T
    l3.append(Stock)
    # Stock.Date = StockLink['Name'][i]

df_Teraz = pd.concat(l3 , axis = 1)
##
a3 = l3[0]
for i in range(1,len(l3)):
    a1 = l3[i]
    a3=pd.merge(a3, a1, on='Name', how='outer')
##
def link_checker(StopChar):
    link = "#ddlTable"
    link = driver.find_element(By.CSS_SELECTOR , link)
    link = link.text

    if StopChar in link:
        return True
    else:
        return False

link_checker("Ã—?«‰")
##
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
##
import requests
from bs4 import BeautifulSoup
import pandas as pd
##
BPL1617 = pd.read_html("https://www.statbunker.com/competitions/FantasyFootballPlayersStats?comp_id=556")
##
url = 'https://codal.ir/Reports/Decision.aspx?LetterSerial=wGjNQQQaQQQFf7eFlmsasI8piA1g%3d%3d&rt=2&let=6&ct=0&ft=-1&sheetId=9'
page = requests.get(url, headers = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            } )
##
soup = BeautifulSoup(page.content, 'html.parser')

tbl = soup.find("table",{"id":"1466"})

data_frame = pd.read_html(str(tbl))[0]

##def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
