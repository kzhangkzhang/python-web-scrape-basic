from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com', verify=False).text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

csv_file = open('kevin_scrape_output.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'youtube link'])

for article in soup.find_all('article'):
    # Get Headline
    headline = article.h2.a.text
    # Get Summary
    summary = article.find('div', class_='entry-content').p.text

    # article may not have youtube
    try:
        # Get Youtube
        video_source = article.find('iframe', class_="youtube-player")['src']

        video_id = video_source.split('/')[4]
        video_id = video_id.split('?')[0]

        # f function is python 3.6 or above
        youtube_link = f'https://youtube.com/watch?v={video_id}'
        print('++ youtube link is ==>', youtube_link)
    except Exception as e:
        youtube_link = 'Article has no youtube'

    # write data to csv file
    csv_writer.writerow([headline, summary, youtube_link])

# close the file
csv_file.close()
