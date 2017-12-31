# Login--Django-1.11
This project implements login and signup functionality in django - 1.11

This project shows how to implement login and signup functionality with custom UI by using Djano-1.11's inbuild authentication views.

Requirements:
1. Python 3.4
2. Django-1.11.5
3. django-sendgrid-v5 (for sending emails)

For setting up sendgrid for emails:
1. Create a sendgrid account and generate a SENDGRID_API_KEY
2. Replace SENDGRID_API_KEY value with your SENDGRID_API_KEY value in settings.py

If you want to use file based email, then uncomment line number 131 and 132, create a folder 'sent_emails' in project folder (at the level of accounts folder) and comment last three lines in settings.py
