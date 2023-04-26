import configparser
import json
import asyncio
import time
from discord_sender import send_message
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")
message_path = 1
old_message = []


def dump_all_messages(client, channel):
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    global message_path
    history = client(GetHistoryRequest(
        peer=channel,
        offset_id=0,
        offset_date=None, add_offset=0,
        limit=5, max_id=0, min_id=0,
        hash=0))
    messages = list(history.messages)
    messages.reverse()
    for message in messages:
        print('go')
        if int(message.id) not in old_message:
            send_message('1097865768793813002', discord_message)
            old_message.append(int(message.id))


def main():
    with open("setting.json", 'r', encoding='utf8') as out:
        setting = json.load(out)

        client = TelegramClient(
            'vip',
            setting['account']['api_id'],
            setting['account']['api_hash']
        )

    client.start()
    url = setting['channels']['source'][0]
    channel = client.get_entity(url)
    while True:
        dump_all_messages(client, channel)
        time.sleep(30)


main()
