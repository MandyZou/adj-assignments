#Set up
import urllib2, csv, mechanize
from bs4 import BeautifulSoup

# Create the output file 
output = open('output.csv','w')
writer = csv.writer(output)

# Open the url
br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')
html = br.response().read()

soup = BeautifulSoup(html, "html.parser")

# Put all values into a list
optionslist = soup.find('select',
    {'name':'ctl00$MainContent$cboCounty',
    'id': 'cboCounty'
})

# Get the option tags
optionslist = optionslist.find_all('option')

# Loop over values in the optionslist
for options in optionslist:
    br.select_form(nr=0)
    br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
    br.form['ctl00$MainContent$cboCounty'] = [options['value']]

    br.submit('ctl00$MainContent$btnCountyChange')

    html = br.response().read()

    #Translate the HTML into a BeautifulSoup object
    soup = BeautifulSoup(html, "html.parser")

    #Find the main table using both the "align" and "class" attributes
    main_table = soup.find('table',
        {'id':'MainContent_dgrdResults'}
    )

    # Set up a output list
    output = []
    output.append(options.text)

     #Now get the data from each table row
    for row in main_table.find_all('tr'):
        data = [cell.text for cell in row.find_all('td')]


        # Select percentages and candidates' names 
        if data:
            if data[0] in ['Hillary Clinton', 'Bernie Sanders', 'Ted Cruz', 'John R. Kasich','Donald J. Trump']:
                output.append(data[3]) 

    print output