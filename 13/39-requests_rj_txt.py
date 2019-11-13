#! python3

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
badRes = requests.get('https://automatetheboringstuff.com/files/rsjdnsajd.txt')

print(res.status_code)
print(badRes.status_code)

badRes.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
