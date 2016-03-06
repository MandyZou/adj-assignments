import csv

csvfile = open('./data/cleanme.csv','r')
outfile = open('./data/clean.csv','w')

reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

writer.writeheader()

for row in reader:
    #all text fields in uppercase
    row['first_name'] = row['first_name'].upper()
    row['mid_init'] = row['mid_init'].upper()
    row['last_name'] = row['last_name'].upper()
    row['addr'] = row['addr'].upper()
    row['city'] = row['city'].upper()
    row['state'] = row['state'].upper()
    #delete any non-breaking spaces
    row['city'] = row['city'].replace('&NBSP;',' ')
    #add leading zero
    row['zip'] = row['zip'].zfill(5)
    #save only contributions of $1000 or more
    if int(row['amount']) >= 1000:
        
        print row
    writer.writerow(row)


