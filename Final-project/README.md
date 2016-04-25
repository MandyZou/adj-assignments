# The final memo for the final project
My final project is to create something like google alert. When the bill has something status changed, it will send out an email to the newsroom (or anyone who use it).

My plan is to scrape ‘last actions’ sections in each bill page and save them into a csv file. Every time when someone runs the code, it will create a new csv and it will compare it to the old csv file. When something is different, it will print out the different part. (Please tell me if my plan is wrong)

I tried it in two ways. One way is by Missouri bill page (http://www.house.mo.gov/billlist.aspx). The other is by API. And I encountered problems with both of them.

1. missouriweb.py
I get the list of bill id from the main page. But when I try to get into every bill page, things get weird. For example, in my bill id list, some bill ids are like “HBs 1366& 1878,” but the actual url for that bill is “http://www.house.mo.gov/billsummary.aspx?bill=HB1366&year=2016&code=R.” 

Therefore, I could not get every number into the url list:
url = 'http://www.house.mo.gov/billsummary.aspx?bill='+names+'&year=2016&code=R'

Because I could not get the right urls, the rest of steps are not working.

2. APIweb2.py
Thanks to our previous assignments, I get the list of bill ids and the url list of page details. But the problem is , there are two different pages, one  for house bill, and the other for senate bill.

First, I don’t know how to separate senate bill pages from house bill pages, and loop over them separately.

Second, I figured out the way to scrape the senate bill page but I don’t know how to choose a specific td (’last action’) from a table without any ids or other attr. 



