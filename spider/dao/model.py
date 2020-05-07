from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BIGINT
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class CountryCode(Base):
    __tablename__ = 'country_code'
    id = Column(Integer, primary_key=True)
    country_code = Column(String(50), nullable=False)
    country = Column(String(100), nullable=False)
    iso_code = Column(String(20), nullable=True)
    population = Column(Integer, nullable=True)
    area = Column(Integer, nullable=True)
    gdp = Column(String(30), nullable=True)
    available = Column(Boolean, nullable=True, default=True)
    area_codes = relationship("AreaCode", back_populates="country_code")


class AreaCode(Base):
    __tablename__ = 'area_code'
    id = Column(Integer, primary_key=True)
    area_code = Column(String(10), nullable=False)
    state = Column(String(50), nullable=True)
    abbreviation = Column(String(10), nullable=True)
    available = Column(Boolean, nullable=True, default=True)
    exchange_codes = relationship("ExchangeCode", back_populates="area_code")
    country_code = relationship("CountryCode", back_populates="area_codes")
    country_code_id = Column(Integer, ForeignKey('country_code.id'))


class ExchangeCode(Base):
    __tablename__ = 'exchange_code'
    id = Column(BIGINT, primary_key=True)
    exchange_code = Column(String(10), nullable=False)
    area_code_and_exchange_code = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    carrier = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    county = Column(String(100), nullable=True)
    zip_code = Column(String(20), nullable=True)
    timezone = Column(String(20), nullable=True)
    available = Column(Boolean, nullable=True, default=True)
    area_code_id = Column(Integer, ForeignKey('area_code.id'))
    area_code = relationship("AreaCode", back_populates="exchange_codes")


class PhoneNumber(Base):
    __tablename__ = 'phone_number'
    id = Column(BIGINT, primary_key=True)
    phone_number = Column(String(20), nullable=False)
    location = Column(String(50), nullable=True)
    description = Column(String(50), nullable=True)
    available = Column(Boolean, nullable=True, default=True)
    exchange_code_id = Column(BIGINT, ForeignKey('exchange_code.id'))