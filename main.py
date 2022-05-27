import schedule
import time, datetime
import requests
import json
import os

from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

Base = declarative_base()

class MystromDevice(Base):

  __tablename__ = 'devices'

  id = Column(Integer, primary_key=True)

  name = Column(String(16))
  ip = Column(String(16))

  # Lets us print out a user object conveniently.
  def __repr__(self):
    return "<Device(id='%s', name='%s', ip='%s')>" % (
            self.id, self.name, self.ip)

class MystromResult(Base):

  __tablename__ = 'results'

  id = Column(Integer, primary_key=True)

  device_id = Column(Integer, ForeignKey('devices.id'))

  power = Column(Float)
  ws = Column(Float)
  relay = Column(Integer)
  temperature = Column(Float)
  date = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)

  # Lets us print out a user object conveniently.
  def __repr__(self):
    return "<Result(deivce_id='%s', power='%s', ws='%s', relay='%s', temperature='%s', date='%s')>" % (
            self.device_id, self.power, self.ws, self.relay, self.temperature, self.date)

def trigger():
    for device in devices:
        request_data_and_store(device)

def get_devices():
    device_query = session.query(MystromDevice)
    return device_query.all()

def request_data_and_store(device):
    response = requests.get(f'http://{device.ip}/report')
    json_response = json.loads(response.text)
    mystrom_result = json_result_to_object(json_response, device)

    session.add(mystrom_result, device)
    session.commit()

    result_query = session.query(MystromResult)
    for result in result_query.all():
        print(result)

def json_result_to_object(json, device):
    return MystromResult(device_id=device.id, power=json["power"], ws=json["Ws"], relay=json["relay"], temperature=json["temperature"])

if __name__ == '__main__':
    sql_url = os.environ['SQL_URL']
    engine = db.create_engine(sql_url)
    connection = engine.connect()

    Base.metadata.create_all(engine) 

    Session = sessionmaker(bind=engine)
    session = Session()
    
    devices = get_devices()

    schedule.every(1).minutes.do(trigger)

    while True:

        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)