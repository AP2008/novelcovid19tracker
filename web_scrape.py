from datetime import date
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

def get_ccii(results):
    '''
    This Function gets the CONFIRMED COVID-19 CASES IN INDIA
    '''
    ccii = results[0].find('span') # Picks only the line with the number of cases
    return int(list(ccii)[0].replace(',', '')) # Returns the number of cases

def get_cdii(results):
    '''
    This Function gets the CONFIRMED COVID-19 DEATHS IN INDIA
    '''
    cdii = results[1].find('span') # Picks only the line with the number of deaths
    return int(list(cdii)[0].replace(',', '')) # Returns the number of deaths

def get_crii(results):
    '''
    This Function gets the CONFIRMED COVID-19 RECOVERIES IN INDIA
    '''
    crii = results[2].find('span') # Picks only the line with number of recovreries
    return int(list(crii)[0].replace(',', '')) # Returns the number of recoveries

# def data_collect_ccii(ccii, loc):
    # '''
    # Collects the data of ccii and sends it to the function 'plot'
    # '''
    # file = open(loc, 'r')
    # text = csv.reader(file, delimiter=',')
    # line = list(text)
    # cases = []
    # dates = []
    # datet = str(date.today().strftime("%d/%m"))
    # for a_v in line:
        # dates.append(a_v[0])
        # try:
            # cases.append(int(a_v[1]))
        # except ValueError:
            # cases.append(a_v[1])
    # file.close()
    # if dates[-1] != datet:
        # cases.append(int(ccii))
        # caset = ccii
        # dates.append(datet)
        # file = open(loc, 'w', newline='')
        # write = csv.writer(file)
        # for i in range(len(cases)):
            # write.writerow([dates[i], str(cases[i])])
        # file.close()
        # print((loc.split('\\')[-1]).replace('.csv', ': '), ccii)
    # elif cases[-1] < ccii:
        # caset = []
        # cases[-1] = (int(ccii))
        # for i_v in cases:
            # caset.append(str(i_v))
        # with open(loc, 'w', newline='') as file:
            # write = csv.writer(file)
            # for i in range(len(cases)):
                # write.writerow([dates[i], str(caset[i])])
            # file.close()
        # print((loc.split('\\')[-1]).replace('.csv', ': '), ccii)
    # dates.pop(0)
    # cases.pop(0)
    # return dates, cases
# URL = 'https://www.worldometers.info/coronavirus/country/india/'

# page = requests.get(URL, verify=False)
# soup = bs(page.content, 'html.parser') #Gets the HTML content using bs4
# results = soup.find_all(id='maincounter-wrap') #Finds all content with id 'maincounter-wrap'

# ci = data_collect_ccii(get_ccii(results), 'C:\work\python\coronacounter\coronacases.csv')
# print(ci)

