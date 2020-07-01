from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from spider.dao.model import CountryCode, AreaCode, ExchangeCode
import os


class Dao(object):

    def __init__(self):
        url = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:postgres@127.0.0.1/pigeon')
        engine = create_engine(url, echo=True)
        session = sessionmaker()
        session.configure(bind=engine)
        self.session = session()

    def get_country_by_code(self, code):
        return self.session.query(CountryCode).filter(CountryCode.country_code == code).first()

    def get_area_by_code(self, code):
        return self.session.query(AreaCode).filter(AreaCode.area_code == code).first()

    def get_exchange_by_code(self, code):
        return self.session.query(ExchangeCode).filter(ExchangeCode.area_code_and_exchange_code == code).first()

    def save(self, obj):
        self.session.add(obj)
        self.session.commit()




