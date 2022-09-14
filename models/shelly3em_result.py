import imp

from pytz import timezone
from base import Base
from sqlalchemy import Column, ForeignKey, Integer, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Shelly3EMResult(Base):

  __tablename__ = 'shelly3em_results'

  id = Column(Integer, primary_key=True)

  device_id = Column(Integer, ForeignKey('shelly3em_devices.id'))

  emeters = relationship('Shelly3EMEmeterResult', backref="result")
  total_power = Column(Float)
  date = Column(DateTime(timezone=True), default=datetime.now)



  # Lets us print out a user object conveniently.
  def __repr__(self):
    return "<EmeterResult(device_id='%s', emeter_id='%s', power='%s', pf='%s', current='%s', voltage='%s', total='%s', total_returned='%s')>" % (
      self.device_id, self.emeter_id, self.power, self.pf, self.current, self.voltage, self.total, self.total_returned)
