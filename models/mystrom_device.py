from base import Base
from sqlalchemy import Column, Integer, String, Boolean

class MystromDevice(Base):

  __tablename__ = 'devices'

  id = Column(Integer, primary_key=True)

  name = Column(String(16))
  ip = Column(String(16))
  active = Column(Boolean)

  # Lets us print out a user object conveniently.
  def __repr__(self):
    return "<Device(id='%s', name='%s', ip='%s', active='%s')>" % (
            self.id, self.name, self.ip, self.active)