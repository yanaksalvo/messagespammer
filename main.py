import threading
import requests
import time

print("")
print("▒█▀▀█ █░░█ █▀▀ █▀▀ █░░█ 　 ▒█░▄▀ ░▀░ █░░ █░░ █▀▀ █▀▀█")
print("▒█▄▄█ █░░█ ▀▀█ ▀▀█ █▄▄█ 　 ▒█▀▄░ ▀█▀ █░░ █░░ █▀▀ █▄▄▀")
print("▒█░░░ ░▀▀▀ ▀▀▀ ▀▀▀ ▄▄▄█ 　 ▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀")

print("                                      Made by certified alihan")
channel = input('Id of channel: ')
message = input('Message to spam: ')
delay = input('Delay: ')

tokens = open("tokens.txt", "r").read().splitlines()


def spam(token, channel, message):
    url = f'https://canary.discord.com/api/v9/channels/{channel}/messages'
    data = {"content": message}
    header = {"authorization": token}

    while True:
        time.sleep(int(0))
        r = requests.post(url, json=data, headers=header)
        print(f"Token {token} - Status Code: {r.status_code}")


def thread(token):
    channel_id = channel
    text = message
    threading.Thread(target=spam, args=(token, channel_id, text)).start()

start = input('Press any key when you are ready ')

for token in tokens:
    thread(token)
