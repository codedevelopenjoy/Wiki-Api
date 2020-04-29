from bs4 import BeautifulSoup
import requests
def scrap(city):
    url = 'https://www.weathercity.com/in/'+city+'/'
    soup = BeautifulSoup(requests.get(url).content,'html5lib')
    data={}
    #TODAY DATA FETCHED======================================================================
    datatemp = {}
    id_ = soup.find('font',class_='fc_summ_h2').text.strip()
    datatemp['name'] = soup.find('font',class_='fc_summ_h1').text.strip()
    datatemp['description'] = soup.findAll('td',class_='fc_summ_c1')[1].text.strip()
    temp = soup.findAll('font',class_='fc_summ_lo')
    if len(temp) == 4:
        datatemp['lowest'] = 'N.A'
    else:
        temp = temp[1:]
        datatemp['lowest'] = temp[0].text.strip()
        
    temp1 = soup.findAll('font',class_='fc_summ_hi')
    if len(temp1) == 4:
        datatemp['highest'] = 'N.A'
    else:
        temp1 = temp1[1:]
        datatemp['highest'] = temp1[0].text.strip()
    data[id_] = datatemp
    #=======================================================================================
    #REST DAYS==============================================================================
    pDesc = soup.findAll('font',class_='fc_summ_h1')
    dDesc = soup.findAll('td',class_='fc_summ_c2')[4:]
    idDesc = soup.findAll('font',class_='fc_summ_h2')[1:]

    for x in range(4):
        datatemp={}
        datatemp['name'] = pDesc[x].text.strip()
        datatemp['description'] = dDesc[x].text.strip()
        datatemp['lowest'] = temp[x].text.strip()
        datatemp['highest'] = temp1[x].text.strip()
        data[idDesc[x].text.strip()] = datatemp
    #=======================================================================================
    return data
