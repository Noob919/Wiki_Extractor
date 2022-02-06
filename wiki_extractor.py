#Required Libaries
import urllib.request
import os
import re
import json
from typing import List
from bs4 import BeautifulSoup

#Getting user's input
keyword = input("Please enter the keyword: \n")
num_url = int(input("Please enter the required number of urls: \n"))

def get_urls(keyword: str, num_url: int) -> List:
    keyword = keyword.replace(' ','+')
    url = f'https://en.wikipedia.org/wiki/Special:Search?search={keyword}'
    page = urllib.request.urlopen(url)
    soup =  BeautifulSoup(page, 'lxml')
    anchor_soup = soup.body.find_all('a')

    #Initializing the empty lisr to store the urls
    urls = []

    #Define patterns to remove those some useless urls using regex module
    pattern1 = re.compile(r'\=')
    pattern2 = re.compile(r'#')
    pattern3 = re.compile(r':')

    #loop to populate the urls list
    for link in anchor_soup:
        u = link.get('href')
        if (u == None):
            urls = urls
        elif(pattern1.search(u)):
            urls = urls
        elif(pattern2.search(u)):
            urls = urls
        elif(pattern3.search(u)):
            urls = urls
        else:
            urls.append(u)
            if (len(urls) == num_url):
                break
    return urls


def get_data(keyword: str, num_url: int) -> List: 
    #Initializing an empty list to store one Paragragh from the page
    p_texts = []

    #Initializing an empty dictionary to get the final json file
    final_dic = {}
    final_list = []
    #Defining the pattern to remove blank p tags
    pattern4 = re.compile(r'\n')

    urls = get_urls(keyword,num_url)
    #Loop to dump all the content in the file(data.json)
    for u in urls:
        page_url = os.path.join('https://en.wikipedia.org'+u)
        page_content = urllib.request.urlopen(page_url)
        page_soup = BeautifulSoup(page_content,'lxml')
        for p in page_soup.body.find_all('p'):
            p = p.get_text()
            p_texts.append(p)
            for i in p_texts:
                if(len(i)>100):
                    final_dic = {"url":page_url,"Paragragh":i}
        final_list.append(final_dic)
        # print(final_dic)
        p_texts.clear()
    with open('data.json', 'a') as fp:
        json.dump(final_list,fp,indent =5)
        fp.close()
    return print("Sucess")


final_list = get_data(keyword,num_url)
