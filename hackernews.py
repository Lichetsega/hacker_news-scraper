import requests
from bs4 import BeautifulSoup
import pprint
import time


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def get_hn_data(pages):
    mega_links = []
    mega_subtext = []
    for i in range(1, pages + 1):
        print(f"Scraping page {i}...")
        res = requests.get(f"https://news.ycombinator.com/news?p={i}")
        soup = BeautifulSoup(res.text, 'html.parser')
        mega_links.extend(soup.select('.titleline'))
        mega_subtext.extend(soup.select('.subtext'))
        time.sleep(0.5)
    return mega_links, mega_subtext


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        anchor_tag = item.find('a')
        href = anchor_tag.get('href', None) if anchor_tag else None
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def create_html_report(hn_list):
    """Generates a clean HTML file from the scraped data."""
    html_content = """
    <html>
    <head>
        <style>
            body { 
                   font-family: sans-serif; 
                   margin: 40px; 
                   background-color: #f6f6ef;
            }
            h1 { 
              color: #ff6600; 
              border-bottom: 2px solid #ff6600; 
              padding-bottom: 10px; 
            }
            .story { 
               background: white; 
               padding: 15px; 
               margin-bottom: 10px; 
               border-radius: 5px;
               box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .title { 
               font-size: 1.2em; 
               font-weight: bold; 
               text-decoration: none; 
               color: #000; 
            }
            .votes { 
               color: #ff6600; 
               font-weight: bold; 
               margin-right: 15px; 
            }
            a:hover { 
              text-decoration: underline; 
            }
        </style>
    </head>
    <body>
        <h1>🔥 Top Hacker News Stories</h1>
    """

    for item in hn_list:
        html_content += f"""
        <div class="story">
            <span class="votes">{item['votes']} pts</span>
            <a class="title" href="{item['link']}" target="_blank">{item['title']}</a>
        </div>
        """

    html_content += "</body></html>"

    with open("my_hn_news.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("\n✅ Success! Open 'my_hn_news.html' in your browser to see your news.")

total_pages = 3
links, subtext = get_hn_data(total_pages)
custom_list = create_custom_hn(links, subtext)

create_html_report(custom_list)