import schedule
import time
import requests
import json

from base import Base, session_factory

from models.mystrom_device import MystromDevice
from models.mystrom_result import MystromResult

@schedule.repeat(schedule.every(1).minutes)
def trigger():
    for device in devices:
        request_data_and_store(device)

def get_devices():
    device_query = session.query(MystromDevice)
    return device_query.all()

def request_data_and_store(device):
    try:
        response = requests.get(f'http://{device.ip}/report')
    except requests.ConnectionError as e:
        print(f'Device {device.name} with ip address {device.ip} seems to be not reachable.')
        return
    except requests.Timeout as e:
        print(f'Request to device {device.name} with ip address {device.ip} timed out.')
        return
    except requests.RequestException as e:
        print(f'Request to device {device.name} with ip address {device.ip} failed.')
        return

    response = json.loads(response.text)
    mystrom_result = MystromResult(device_id=device.id, power=response["power"], ws=response["Ws"], relay=response["relay"], temperature=response["temperature"])

    session.add(mystrom_result, device)
    session.commit()

if __name__ == '__main__':
    session = session_factory()
    devices = get_devices()

    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)
