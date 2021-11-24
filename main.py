import pandas as pd
from get_value import get_value
from notification import send_text


def sensors_value(sensor_table, tag):
    return sensor_table[tag].iloc[-1]  # last row value


def query_event(plant, sheet, sensor_table):  # each rows
    texts = []
    for index, row in sheet.iterrows():
        print(f'  row :  {index} ')
        status = row['Status']
        message = row['Message']
        tag = row['Tags']
        if status != 'on':
            continue
        value = sensors_value(sensor_table, tag)
        txt = message + ' : ' + str(value)
        print(f'    message : {message}')
        print(f'    value : {value}')
        texts.append(txt)
    print(f'texts : {texts}')
    send_text(texts, plant)  # Send Massage to ms-team


if __name__ == '__main__':
    # read_data
    input_path = get_value('Input_path')
    sensorsdata = get_value('Sensors_data')
    for plant in get_value('All_Plant'):  # each plant
        print(f'{plant} :')
        sheet = pd.read_excel(
            input_path, sheet_name=plant)  # read input sheet
        sensor_table = pd.read_csv(sensorsdata)  # read data mock
        query_event(plant, sheet, sensor_table)
