import schedule
import time
import requests
import json

from base import Base, session_factory

from models.shelly3em_device import Shelly3EMDevice
from models.shelly3em_emeter_result import Shelly3EMEmeterResult
from models.shelly3em_result import Shelly3EMResult

@schedule.repeat(schedule.every(1).minute)
def trigger():
    for device in get_active_devices():
        request_data_and_store(device)

def get_active_devices():
    device_query = session.query(Shelly3EMDevice).filter(Shelly3EMDevice.active == True)
    return device_query.all()

def request_data_and_store(device):
    try:
        response = requests.get(f'http://{device.ip}/status')
    except requests.ConnectionError as e:
        print(f'Device {device.name} with ip address {device.ip} seems to be not reachable.')
        return
    except requests.Timeout as e:
        print(f'Request to device {device.name} with ip address {device.ip} timed out.')
        return
    except requests.RequestException as e:
        print(f'Request to device {device.name} with ip address {device.ip} failed.')
        return

    try:
        response = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        print(f'Request to device {device.name} with ip address {device.ip} returns invalid JSON response.')
        return

    shelly_result = Shelly3EMResult(device_id=device.id, total_power=response["total_power"])
    emeters = response["emeters"]
    emeter0 = emeters[0]
    emeter1 = emeters[1]
    emeter2 = emeters[2]
    emeter0_result = Shelly3EMEmeterResult(result=shelly_result, emeter_id=0, power=emeter0["power"], pf=emeter0["pf"], current=emeter0["current"], voltage=emeter0["voltage"], total=emeter0["total"], total_returned=emeter0["total_returned"])
    emeter1_result = Shelly3EMEmeterResult(result=shelly_result, emeter_id=1, power=emeter1["power"], pf=emeter1["pf"], current=emeter1["current"], voltage=emeter1["voltage"], total=emeter1["total"], total_returned=emeter1["total_returned"])
    emeter2_result = Shelly3EMEmeterResult(result=shelly_result, emeter_id=2, power=emeter2["power"], pf=emeter2["pf"], current=emeter2["current"], voltage=emeter2["voltage"], total=emeter2["total"], total_returned=emeter2["total_returned"])

    session.add(shelly_result)
    session.commit()
    session.add(emeter0_result)
    session.add(emeter1_result)
    session.add(emeter2_result)
    session.commit()

if __name__ == '__main__':
    session = session_factory()

    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)
