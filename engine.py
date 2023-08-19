from sqlalchemy import create_engine, Column, String, Float, INTEGER
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime, timedelta
from config import DATABASE_URL
import requests
from config import cityList, coordList
from config import BASE_URL, API_TOKEN

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class CityClimateModel(Base):
    __tablename__ = 'climate'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String)
    dt = Column(String)
    temp = Column(Float)
    wind_speed = Column(Float)
    pressure = Column(Float)
    humidity = Column(Float)


def Get_And_Save():
    CityClimateResponse = []
    for city, cord in zip(cityList, coordList):
        for i in range(5):
            today=datetime.today()+timedelta(days=-i)
            today = int(datetime.timestamp((today)))
            response = requests.get(f"{BASE_URL}{cord}&dt={today}&appid={API_TOKEN}")
            if response.status_code == 200:
                response = response.json()
                current = response["current"]
                data = {
                    'dt': current['dt'],
                    'name': city,
                    'temp': current["temp"],
                    'wind_speed': current["wind_speed"],
                    'pressure': current["pressure"],
                    'humidity': current["humidity"],
                }
                CityClimateResponse.append(data)
                for cityHorly in response["hourly"]:
                    data = {
                        'dt': cityHorly["dt"],
                        'name': city,
                        'temp': cityHorly["temp"],
                        'wind_speed': cityHorly["wind_speed"],
                        'pressure': cityHorly["pressure"],
                        'humidity': cityHorly["humidity"]
                    }
                    CityClimateResponse.append(data)
            print(f"Actualization: {i+1}/5 in {city}")
    return CityClimateResponse
