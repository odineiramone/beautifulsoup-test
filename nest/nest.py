import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime

def metro_spider():
    page = spider_man('http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx')
    subway_lines = page.find_all(id = 'statusLinhaMetro')
    subway_updated_at = page.find_all(id = 'statusLinhaMetro')
    subway_viaquatro_updated_at = page.find_all(id = 'statusLinhaMetro')
    parsed_result = []

    for lines in subway_lines:
        for li in lines.find_all('li'):
            spans =  li.find_all('span')
            parsed_result.append({
                'situacao' : error_handler(spans[1]),
                'linha'    : spans[0].string
            })

    last_update = {
        'metro' :filter_datetime( page.find(id = 'dataAtualizacaoStatus').text),
        'viaquatro' : filter_datetime(page.find(id = 'dataAtualizacaoStatusViaQuatro').text)
    }

    return [parsed_result, last_update]

def error_handler(span):
    try:
        return span.string.strip(' \t\n\r')
    except AttributeError:
        return span.find('a').string


def cptm_spider():
    page = spider_man('http://www.cptm.sp.gov.br/Pages/Home.aspx')
    cptm_lines = page.find(class_= 'situacao_linhas')

    divs = cptm_lines.div.find_all('div')
    divs = divs[:-1]

    parsed_result = []

    for div in divs:
        spans = div.find_all('span')
        parsed_result.append({
            'situacao' : spans[1].string,
            'linha'    : "Linha {line_title}".format(line_title=spans[0].string.capitalize())
        })

    last_update = filter_datetime(page.find(class_= 'ultima_atualizacao').text)

    return [parsed_result, last_update]


def spider_man(url):
    page = urlopen(url).read()
    return BeautifulSoup(page, 'html.parser')


def filter_datetime(text):
    p = re.compile('[0-9]+/[0-9]+/[0-9]+.*[0-9]+:[0-9]+')
    match = p.search(text)
    if match:
        return match.group(0)
    else:
        return ''


def go_spidey():
    metro_status, metro_updated_at = metro_spider()
    cptm_status, cptm_updated_at = cptm_spider()

    result = {
        'metro' : {
            'status' : metro_status,
            'updated_at' : metro_updated_at
        },
        'cptm' : {
            'status' : cptm_status,
            'updated_at' : cptm_updated_at
        },
        'now_is' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return result


if __name__ == '__main__':
    go_spidey()
