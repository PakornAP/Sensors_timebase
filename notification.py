import pymsteams
from get_value import get_value
from time import strftime
from datetime import datetime


def send_text(texts, plant):
    # connect with web hooks in yaml file
    Webhooks_URL = get_value('Webhooks_URL')
    myTeamsMessage = pymsteams.connectorcard(Webhooks_URL)
    # Time report
    now_time = datetime.now()
    now_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
    date_time = 'Datetime : ' + now_time
    myTeamsMessage.title('Plant : ' + plant)
    # Add text to the message.
    n_line = '   \n'
    result = ''
    # list of message
    for txt in texts:
        result = result+txt+n_line
    myTeamsMessage.text(date_time + n_line + result)
    # send the message.
    myTeamsMessage.send()
