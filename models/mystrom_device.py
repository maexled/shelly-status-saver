from base import Base
from sqlalchemy import Column, Integer, String

class MystromDevice(Base):

  __tablename__ = 'devices'

  id = Column(Integer, primary_key=True)

  name = Column(String(16))
  ip = Column(String(16))

  # Lets us print out a user object conveniently.
  def __repr__(self):
    return "<Device(id='%s', name='%s', ip='%s')>" % (
            self.id, self.name, self.ip)