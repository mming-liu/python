import re
import requests
from bs4 import BeautifulSoup

def select_text(table):
    tag = []
    texts = bsObj.select(table)
    for text in texts :
        text = text.get_text().strip()
        tag.append(text)
    return tag

def del_elements(text,str1,str2):
    for i in text:
        if i == str1 or i == str2:
            context.remove(i)
    return text

if __name__ == '__main__' :
    url = 'http://www.qiushibaike.com/hot/page/1'
    response = requests.get(url,verify = False)
    dict = {}
    bsObj = BeautifulSoup(response.text,"html.parser")
    author = select_text('h2')
    # print(len(author))
    # print(author)
    context = select_text('html body div div div div a div span')
    re = re.compile(r'.*?：$')
    context = del_elements(context,'','查看全文')
    context = [i for i in context if not re.match(i)]
    # print(len(context))
    # print(context)
    for m in author:
        for n in context:
            if author.index(m) == context.index(n) :
                dict[m] = n
    print(dict)