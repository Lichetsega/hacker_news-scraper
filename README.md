Hackernews-Signal-Filter is a lightweight Python tool that cleans up your Hacker News experience. 
Instead of scrolling through pages of low-engagement posts, this script scrapes multiple pages, filters for high-quality content (100+ points), and presents them in a beautifully sorted list.

🚀 Key Features 

 - Visual Reports:Generates a clean, styled HTML file for a better reading experience.
 - Multi-Page Scraping: Dynamically crawls through the first n pages of Hacker News.
 - Quality Filtering: Only shows "Signal" stories (those with a score > 99).
 - Ranked Results: Automatically sorts stories by vote count so the most important news is at the top.
 - Ethical Scraping: Implements time.sleep() to ensure the script respects Hacker News' servers.

🛠️ Installation

Make sure you have Python 3 installed.
Clone the repo:
Bash ->  git clone https://github.com/lichetsega/hacker_news-scraper.git 
     ->  cd hacker_news-scraper
Install the required libraries:
Bash ->  pip install requests beautifulsoup4

🖥️ Usage

Simply run the script using Python:
Bash  ->  python hackernews.py
You can adjust the total_pages variable in the script to scrape as much of the archive as you want.

🧠 How it Works

The script follows a simple Request -> Parse -> Filter -> Sort-> Export pipeline:
 - Request: Uses the requests library to fetch the HTML content of news.ycombinator.com/news?p={i}.
 - Parse: Uses BeautifulSoup with CSS selectors to target specific elements:
     .titleline: To extract the story title and link.
     .subtext: To find the corresponding score (points).
 - Filter: The script matches titles to scores using enumerate and keeps only those where points > 99.
- Sort: It uses a lambda function to sort the final list of dictionaries:
     sorted_list = sorted(data, key=lambda k: k['votes'], reverse=True)📄
-  Export:Wraps the filtered data in a custom CSS template and writes it to a local 'my_hn_news.html' file.
