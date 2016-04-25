import urllib2, json, urllib,csv, mechanize, requests
import urlparse
from urllib import urlencode
from bs4 import BeautifulSoup

br = mechanize.Browser()

# output = open('ApiList.csv','w')
# writer = csv.writer(output, delimiter = ",")

# writer.writerow(['bill_id','primary sponsor','bill_title'])


response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&search_window=session').read()

bills = json.loads(response)


# Set up a list, in order to put all Json code into a list (after read each bill_detail page)
bill_re = []

for bill in bills:

    # This is the processing piece I mentioned in the assignment description. To include
    # a bill ID (which has spaces in it)through a URL in Python, you need to do this first.
    encoded_bill_id = urllib.quote(bill['bill_id'])

    # Put a list of bill id into url
    url = 'http://openstates.org/api/v1/bills/mo/2016/'+encoded_bill_id+'/?apikey=1f366e0712bd4ad6b079afe3bb993434'

    # Read each bill_detail page
    bill_page = urllib2.urlopen(url).read()

    bill_detail = json.loads(bill_page)

    bill_re.append(bill_detail)

    
    # Get sponsor, title, id from each page
    for bill_detail in bill_re:

        bill_source = bill_detail['sources']

        # bill_link = urllib2.urlopen(bill_source).read()

        # details = json.loads(bill_link)

        # Get the first url in every page
        first_url = bill_source[:1]

    # print first_url

        # Get the url from a list first, then from a dictionary
        for link_dic in first_url:
            links = link_dic.values()

            for bill_url in links:
                bill_links = bill_url.encode('utf-8')

                # Run the list of urls by requests
                # The problem is that there are two different pages, one for SB, the other fo HB. How should I separate them?
                # The following is the SB page
                bill_details = requests.get(bill_links)
                soup = BeautifulSoup(bill_details.content, "html.parser")


                # find the last actions part in the very page
                main_table = soup.find('table',
                    {'id':'Table3'}
                    )

                for row in main_table.find_all('tr'):
                    info = [cell.text for cell in row.find_all('td')]

                    for rows in info:
                        get_info = soup.find('span',
                            {'id':'lblLastAction'}
                            )

                        last = [cell.text for cell in get_info]

                        for rowss in last:
                            last_actions = rowss.encode('utf-8')

                # print last_actions

                second_table = soup.find('table',
                    {'id':'Table1'}
                    )

                for rowsss in second_table.find_all('tr'):
                    infor = [cell.text for cell in row.find_all('td')]

                    for rowssss in infor:
                        get_name = soup.find('span',
                            {'id':'lblBillNum'}
                            )

                        bill_name = [cell.text for cell in get_name]

                # print bill_name

                        for cells in bill_name:
                            bill_ids = cells.encode('utf-8')

                # print last_actions, bill_ids
                # End of the SB page

                # The following is the HB page
                main_table2 = soup.find('table')

                bill_tr = main_table.find_all('tr')
                    

                # I don't know how to select specific td from the table without any id or other attr. 

                # bill_td = bill_tr[3]

                # print bill_td



                


                # bill_rere = []

                # bill_details = mechanize.Browser()
                # br.open(bill_links)
                # html = br.response().reach()

                # soup = BeautifulSoup(html, "html.parser")

                # # bill_info = json.loads(bill_details)

                # bill_rere.append(bill_details)

                    # for infopage in bill_rere:






                # br = mechanize.Browser()
                # br.open('bill_links')
                # html = br.response().read()

                # soup = BeautifulSoup(html, "html.parser").read()



            # print bill_links





            # First, I try to set an alarm based on the condition of "next hearing." But then, I realized that Senate bill doesn't have the "next hearing." Therefore, I have to use "last action," which appears in both Senate Bill and House Bill.





        
        



           

                




    #     for sponsors in sponsor_detail:

    #         # Remember to encode('utf-8'), get rid of "u"
    #         sponsor_name = sponsors['name'].encode('utf-8')
    #         title_name = bill_detail['title'].encode('utf-8')
    #         official_title = bill_detail['bill_id'].encode('utf-8')

    # # print official_title, sponsor_name, title_name
    # writer.writerow([official_title, sponsor_name, title_name])