import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
cities = pd.read_csv("ML Main\california_cities.csv")

lat, lon = cities["latd"], cities["longd"]
population, area = cities["population_total"], cities["area_total_km2"]

plt.scatter(lon, lat, c=np.log10(population), cmap = "Accent", s=area, alpha=0.5)
plt.title("California Cities: Area and Population")
plt.xlabel("lognitude")
plt.ylabel("latitude")
plt.colorbar(label= "Log$_{10}$(polulation)")
plt.show()