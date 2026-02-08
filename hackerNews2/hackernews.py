import requests
from bs4 import BeautifulSoup
import pprint
def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key=lambda k:k['votes'],reverse=True)
def get_hn_data(pages):
    mega_links=[]
    mega_subtext=[]

    for i in range (1 ,pages+1):
        print(f"scraping page {i}...")
        res=requests.get(f"https://news.ycombinator.com/news?p={i}")
        soup=BeautifulSoup(res.text,'html.parser')

        mega_links.extend(soup.select('.titleline'))
        mega_subtext.extend(soup.select('.subtext'))

    return mega_links,mega_subtext
def create_custom_hn(links,subtext):
    hn=[]
    for idx,item in enumerate(links):
        title =item.getText()
        anchor_tag=item.find('a')
        href=anchor_tag.get('href',None) if anchor_tag else None

        vote=subtext[idx].select('.score')
        if len(vote):
            points=int(vote[0].getText().replace("points",""))
            if points > 99:
                hn.append({'title':title,'links':href,'votes':points})
    return sort_stories_by_votes(hn)
total_pages=5
all_links,all_subtext=get_hn_data(total_pages)
custom_list=create_custom_hn(all_links,all_subtext)
pprint.pprint(custom_list)
print(f"total pages found with 100+ points :{len(custom_list)}")