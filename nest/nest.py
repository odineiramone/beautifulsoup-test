from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime

def metro_spider():
    page = spider_man('http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx')
    subway_lines = page.find_all(id = 'statusLinhaMetro')
    parsed_result = []

    for lines in subway_lines:
        for li in lines.find_all('li'):
            spans =  li.find_all('span')
            parsed_result.append({
                'situacao' : spans[1].string.strip(' \t\n\r'),
                'linha'    : spans[0].string
            })

    return parsed_result


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

    return parsed_result


def spider_man(url):
    page = urlopen(url)
    return BeautifulSoup(page, 'html.parser')


def go_spidey():
    result = {
        'status': [
            { 'metro' : metro_spider() },
            { 'cptm' : cptm_spider() },
        ],
        'now_is' : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return result


if __name__ == '__main__':
    go_spidey()
