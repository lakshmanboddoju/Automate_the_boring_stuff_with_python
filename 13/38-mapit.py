#! python3

import webbrowser, sys, pyperclip



if len(sys.argv) > 1:
    # ['mapit.py', '870', 'First', 'St.']
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
