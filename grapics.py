import matplotlib.pyplot as plt
from engine import CityClimateModel, session
from datetime import datetime 

def render():
    result = session.query(CityClimateModel).all()
    x= []
    y= []
    while result:
        print(result.dt)
        # if res.name == "London":
        #     x.append(datetime.fromtimestamp(int(res.dt)))
        #     y.append(res.temp)
        # else:
        #     plt.plot(x, y)


