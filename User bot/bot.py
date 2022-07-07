from telethon import TelegramClient, sync, events
from datetime import date
from Collecting import days, texts, months, usernames
from setup_file import api_id, api_hash
import time

def deleting_zero(string):
    if string[0] == '0':
        return int(string[1:])


client = TelegramClient('checking birthday', api_id, api_hash)
client.start()

while True:

    today = str(date.today())
    today = today.split('-')
    day = today[2]
    month = today[1]
    day = deleting_zero(day)
    month = deleting_zero(month)

    for index_for_all_of_the_lists in range(len(months)):
        if day == int(days[index_for_all_of_the_lists]) and month == int(months[index_for_all_of_the_lists]):
            client.send_message(usernames[index_for_all_of_the_lists],
                                texts[index_for_all_of_the_lists])
    time.sleep(86400)