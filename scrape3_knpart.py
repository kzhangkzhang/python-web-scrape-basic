from bs4 import BeautifulSoup
import requests
import csv

source = requests.get(
    'https://www.knowles.com/subdepartment/dpt-microphones/subdpt-sisonic-surface-mount-mems', verify=False).text

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify().encode('utf8'))

csv_file = open('kevin_scrape_knpart.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['part', 'interface-type', 'port-location'])

for product in soup.find_all('tr', class_='model-item'):
    # Get Part Number
    part = product.find('td', class_='model-id').text
    # Get interface_type
    interface_type = product.find(
        'td', class_='name').find_next_sibling("td").text.strip()
    print('+++ interface_type number ==> ', interface_type)
    # Port Location
    port_location = product.find('td', class_='name').find_next_sibling(
        "td").find_next_sibling("td").text.strip()
    print('+++ port_location number ==> ', port_location)

    # write data to csv file
    csv_writer.writerow([part, interface_type, port_location])

# close the file
csv_file.close()
