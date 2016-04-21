import urllib2, json, urllib,csv
import urlparse
from urllib import urlencode

output = open('ApiList.csv','w')
writer = csv.writer(output, delimiter = ",")

writer.writerow(['bill_id','primary sponsor','bill_title'])


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

        sponsor_detail = bill_detail['sponsors']

        for sponsors in sponsor_detail:

            # Remember to encode('utf-8'), get rid of "u"
            sponsor_name = sponsors['name'].encode('utf-8')
            title_name = bill_detail['title'].encode('utf-8')
            official_title = bill_detail['bill_id'].encode('utf-8')

    # print official_title, sponsor_name, title_name
    writer.writerow([official_title, sponsor_name, title_name])