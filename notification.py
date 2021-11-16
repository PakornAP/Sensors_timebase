import pymsteams
from get_value import get_value
from time import strftime
from datetime import datetime


def send_text(texts, plant):
    # You must create the connectorcard object with the Microsoft Webhook URL
    Webhooks_URL = get_value('Webhooks_URL')
    myTeamsMessage = pymsteams.connectorcard(Webhooks_URL)
    # Add title
    now_time = datetime.now()
    now_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
    date_time = 'Datetime : ' + now_time
    myTeamsMessage.title('Plant : ' + plant)
    # Add text to the message.
    n_line = '   \n'
    result = ''
    for txt in texts:
        result = result+txt+n_line
    myTeamsMessage.text(date_time + n_line + result)
    # send the message.
    myTeamsMessage.send()
