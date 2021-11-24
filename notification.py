import pymsteams
from get_value import get_value
from time import strftime
from datetime import datetime


def send_text(texts, plant):
    # connect with web hooks in yaml file
    # Webhooks_URL = get_value('Webhooks_URL')
    Webhooks_URL = get_value('All_HooksURL')[plant]
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
    footer = n_line+'Production rate is a value at message sending time'
    myTeamsMessage.text(date_time + n_line + result + n_line+footer)
    # send the message.
    myTeamsMessage.send()
