#! python3

### Full documentation at https://imapclient.readthedocs.org
### https://www.magiksys.net/pyzmail
### https://automatetheboringstuff.com/chapter16


import imapclient, pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('personal@gmail.com', 'password')

print(conn.list_folders())
conn.select_folder('INBOX', readonly = True)

# Ids are mapped to each email
# format for search from https://imapclient.readthedocs.io/en/master/_modules/imapclient/imapclient.html#IMAPClient.search
UIDs = conn.search([u'SINCE', datetime.date(2019, 9, 20)])
rawMessage = conn.fetch([2], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[2][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))

# Checking if it was a plaintext email or a html email
print(message.text_part)
print(message.html_part)

# Print email
print(message.text_part.get_payload().decode('UTF-8'))


# Deleting mail
UIDs = conn.search([u'SINCE', datetime.date(2019, 11, 15)])
conn.delete_messages([UIDs[-1]])

conn.logout()
