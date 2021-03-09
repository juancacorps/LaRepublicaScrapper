import requests
import lxml.html as html
import os
import datetime

XPATH_LINK_TO_ARTICLE = '//text-fill/a/@href'
XPATH_TITLE = '//div[@class="mb-auto"]//text-fill//span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p/text()'
XPATH_AUTOR = '//div[@class="autorArticle"]/p/text()'
XPATH_DATEPOST_ARTICLE = '//div[@class="d-flex align-items-end"]/span[@class="date"]/text()'
XPATH_LINK = 'https://www.larepublica.co/' 


def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)
            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('"','').replace('.','').replace(':','')

                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)
                try:
                    author = parsed.xpath(XPATH_AUTOR)[0]
                except:
                    author = 'Anonimo'
                try:
                    date = parsed.xpath(XPATH_DATEPOST_ARTICLE)[0]
                except:
                    date = datetime.date.today()
            except Exception as e:
                print(f'error: {e}')

            with open(f'{today}/{title}.txt','w',encoding='utf-8') as f:
                f.write(date)
                f.write('\n')
                f.write(title)
                f.write('\n \n')
                f.write(summary)
                f.write('\n \n')
                for p in body:
                    f.write(p)
                    f.write('\n')
                f.write('\n \n')
                f.write(f'Noticia escrita por: {author}')

        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as VE:
        print(VE)


def parse_home():
    try:
        response = requests.get(XPATH_LINK)
        if response.status_code == 200:
            home = response.content.decode('utf-8') # Format html
            parsed = html.fromstring(home) # For use expressions html
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)
            for link in links_to_notices:
                parse_notice(link,today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as VE:
        print(VE)


def run():
    parse_home()


if __name__ == '__main__':
    run()