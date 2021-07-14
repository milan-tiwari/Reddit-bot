"""
This web scrapper will list all popular old mustangs with links.
All data is in mustangs.txt
"""

from bs4 import BeautifulSoup as bs
import requests, lxml

html = str(requests.get("https://www.supercars.net/blog/tag/muscle-car/").content)
soup = bs(html, 'lxml')


def top_mustangs():

    with open('mustangs.txt', 'w+') as fl:
        for article in soup.find_all('article'):

            title = article.find('div', class_='meta').h3.a.string
            link = article.find('div', class_='meta').h3.a['href']


            #extracting description from read more link
            html2 = str(requests.get(link).content)
            soup2 = bs(html2, 'lxml')
            article2 = soup2.find('article', class_=None)
            flag = 1


            #checking if the article exists
            if(article2.find('div', class_='copy-paste-block')):
                block = article2.find('div', class_='copy-paste-block')
                desc = ""
                if(block.find('span', id="intelliTXT")):
                    desc = block.find('span', id="intelliTXT").string
                    #writing all extracted data into mustangs.txt with description
                    fl.write(str(title) + ": \n" + desc + "\n" + link + "\n\n")
                    print(str(title) + ": \n" + desc + "\n" + link + "\n\n")
                    flag = 0


            #writing all extracted data into mustangs.txt without description
            if(flag):
                print(str(title) + ": \n" + link + "\n\n")
                fl.write(str(title) + ": \n" + link + "\n\n")


if __name__ == '__main__':
    top_mustangs()
