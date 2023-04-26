import requests

TOKEN = 'MTA5ODI5OTAzMjMxODc5MTc1MQ.GgMsJU.SCntO72Jso3_RUXA8Zr0z4pByYFHMQiRfsc5nw'


def send_message(channel_id: str, message: str):
    headers = {
        'Authorization': f'Bot {TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'content': message
    }
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()


if __name__ == '__main__':
    send_message('1097866060964823060', 'test')

