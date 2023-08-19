import pandas as pd
from engine import Get_And_Save, engine, Base
from pandas import json_normalize
from config import PATH
from grapics import render


def main():
    try:
        Base.metadata.create_all(engine)
        print("Base de datos correcta")

    except ValueError:
        return print(ValueError)
    
    render()
    
    # citys_data = Get_And_Save()
    # if citys_data:
    #     df_climate = pd.DataFrame(citys_data, columns=['dt','name', 'temp', 'pressure', 'wind_speed', 'humidity'])
    #     with engine.connect() as conn:
    #         df_climate.to_sql('climate', conn, if_exists='append', index=False)
    #         print("Datos almacenados correctamente")

    #     normalized_data = json_normalize(citys_data)
    #     with open(f"{PATH}\Climate.cvs", "w") as output_cvs:
    #         normalized_data.to_csv(output_cvs, index=False)
    #         print("archivo guardado correctamente")


if __name__ == "__main__":
    main()
