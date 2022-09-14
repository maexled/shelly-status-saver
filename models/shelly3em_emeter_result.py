from base import Base
from sqlalchemy import Column, ForeignKey, Integer, Float

class Shelly3EMEmeterResult(Base):

  __tablename__ = 'shelly3em_emeter_results'

  id = Column(Integer, primary_key=True)

  result_id = Column(Integer, ForeignKey('shelly3em_results.id'))

  emeter_id = Column(Integer)
  power = Column(Float)
  pf = Column(Float)
  current = Column(Float)
  voltage = Column(Float)
  total = Column(Float)
  total_returned = Column(Float)

  # Lets us print out a user object conveniently.
  def __repr__(self):
    return "<EmeterResult(device_id='%s', emeter_id='%s', power='%s', pf='%s', current='%s', voltage='%s', total='%s', total_returned='%s')>" % (
      self.device_id, self.emeter_id, self.power, self.pf, self.current, self.voltage, self.total, self.total_returned)
