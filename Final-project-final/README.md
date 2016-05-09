# Final-project-final
My final project is to create something like google alert. When the bill has something status changed, it will send out an email to the newsroom (or anyone who use it).

My plan is to scrape ‘last actions’ sections in each bill page and save them into a csv file. Every time when someone runs the code, it will create a new csv and it will compare it to the old csv file. When something is different, it will print out the different part.

I ended with two different versions of the application.

(1) Combined version
The problem of this version is that if you try so many times of the script, you will see the error of “4.7.0 Too many login attempts, please try again later.” If you have an administration account of the gmail, you can change the email limits.

    See the instruction: https://support.google.com/a/answer/2789146

(2) Separate version
First, run the scrape code to get today’s changes.
Second, run the email code to send out the email. The csv file will be sent out with the email.
