# Scrape Set up
import urllib2, json, urllib,csv, mechanize, requests, ast
import urlparse
from urllib import urlencode
from bs4 import BeautifulSoup
import time
from datetime import datetime
# Email alert Set up
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

# Sender address
fromaddr = "annahunder@gmail.com"
# Receiver address
toaddr = "mandyzou02@gmail.com"
 
msg = MIMEMultipart()

# Details about the email 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Today's bill change"

# The body text of the email 
body = "Hi, here are the Missouri bill changes for today."

# Create the result csv file
output = open('BillChange.csv','w')
writer = csv.writer(output)

writer.writerow(['bill_id','bill_title','date','action'])

# Set up email attachment
msg.attach(MIMEText(body, 'plain'))
 
filename = "BillChange.csv"
attachment = open("BillChange.csv", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 

today_time = datetime.utcnow().strftime('%Y-%m-%d 00:00:00')

br = mechanize.Browser()

# output = open('ApiList.csv','w')
# writer = csv.writer(output, delimiter = ",")

# writer.writerow(['bill_id','primary sponsor','bill_title'])


response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&search_window=session').read()

bills = json.loads(response)


# Set up a list, in order to put all Json code into a list (after read each bill_detail page)
bill_re = []

# Set up another list to save the final result
bill_final = []

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

        bill_actions = bill_detail['actions']

        last_one = bill_actions[-1]

    # print last_one

        # Get rid of 'u' in a dict
        bill_action = ast.literal_eval(json.dumps(last_one))

        bill_the_action = bill_action['action']

    # print bill_action
        bill_date = bill_action['date']

        bill_print_id = bill_detail['bill_id'].encode('utf-8')

        bill_print_title = bill_detail['title'].encode('utf-8')

    # print bill_date
    if bill_date == today_time:

        writer.writerow([bill_print_id, bill_print_title, bill_date, bill_the_action])
    
    # Send the email alert!
    msg.attach(part)
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "12334456")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


