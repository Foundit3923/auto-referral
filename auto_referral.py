import smtplib
print('Enter the ID and email spearated by a space: ')
chunks = input().split(' ')

job_id = chunks[0]

received_email = chunks[1]

gmail_user = 'email@email.com'
gmail_password = 'P@ssword'

sent_from = gmail_user
to = [received_email]
subject = 'Referal to %s from Paul Austin'%(job_id)
body = 'This is the body of the message. Go to https://www.google.com'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:
    print('Something went wrong...')
