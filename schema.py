from sqlalchemy import Column, Integer, String, Boolean, Text, Float, \
    create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///identifier.sqlite')


class Apartment(Base):
    __tablename__ = 'apartment'

    id = Column(Integer, primary_key=True)
    settlement = Column(String)
    under_construction = Column(Boolean, nullable=False, default=False)
    description = Column(Text, nullable=False, default='')
    price = Column(Integer, nullable=False, default=0)
    oblast_district = Column(String)
    living_area = Column(Float)
    has_balcony = Column(Boolean, nullable=False, default=False)
    address = Column(String, nullable=False, default='')
    construction_year = Column(Integer)
    rooms_number = Column(Integer, nullable=False, default=1)
    promise_area = Column(Float)
    outer_id = Column(Integer, nullable=False, unique=True, index=True)
    is_active = Column(Boolean, nullable=False, default=True)

    def __str__(self):
        return "<Квартира {}>".format(self.outer_id)


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
