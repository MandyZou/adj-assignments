# Set up
import urllib2, mechanize 
from bs4 import BeautifulSoup
import re, urlparse
from urllib import urlencode


# Open the url 
br = mechanize.Browser()
br.open('http://www.house.mo.gov/billlist.aspx')
html = br.response().read()

# Read the html
soup = BeautifulSoup(html, "html.parser")

# Find the main table
bill_list = soup.find('table',
    {'id':'billAssignGroup',
    'border':'0',
    'width':'100%',
    })

# print bill_list

# find the bill list
for row in bill_list.find_all('tr'):
    bills = [cell.text for cell in row.find_all('a')]

# Only pick the bill name
    bill_name = bills[:1]

# Set up a list, in order to put all Json code into a list (after read each bill_detail page)
    bill_re = []


    for names in bill_name:
# Get rid of the 'u' and '[]'
        names = names.encode('utf-8')

    # print names

        url = 'http://www.house.mo.gov/billsummary.aspx?bill='+names+'&year=2016&code=R'

        print url

        # URL has some problems, so the rest of steps cannot work out
        
        # Read each bill_detail page
        # bill_page = urllib2.urlopen(url).read()

        # bill_detail = json.loads(bill_page)

        # # bill_re.append(bill_detail)

        # print bill_page
    
   


            

#     print bills

# for row in bill_list.find_all('th'):

#     bill_link = soup.find_all('a')

#     for rows in bill_link:
#         bill_href = soup.find_all('href')

#         print bill_href



    # for links in bill_link:

    #     result = num_there(links)

    # print bill_link






