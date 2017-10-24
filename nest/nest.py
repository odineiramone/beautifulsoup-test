from bs4 import BeautifulSoup
from urllib.request import urlopen

def spider_mano():
    page = urlopen('http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx')
    soup = BeautifulSoup(page, 'html.parser')
    subway_lines = soup.find_all(id = 'statusLinhaMetro')
    parsed_result = []

    for lines in subway_lines:
        for li in lines.find_all('li'):
            spans =  li.find_all('span')
            parsed_result.append({
                'situacao' : spans[1].string.strip(' \t\n\r'),
                'linha'    : spans[0].string
            })

    return parsed_result

if __name__ == '__main__':
    spider_mano()
