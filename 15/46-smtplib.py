#! python3

import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('personal@gmail.com', 'password')

conn.sendmail('personal@gmail.com', 'personal@gmail.com', 'Subject: So long...\n\nDear,\nSo long, and thanks for all the monies.\n\n-Lala')

conn.quit()
