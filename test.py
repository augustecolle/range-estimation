import trajectory as tr
import cyclist as cl
import weather as wh
import imp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

imp.reload(tr)
imp.reload(cl)
imp.reload(wh)

route = tr.traject()
route.importGPSData('./routes/waregem.txt')
start = route.get_startPosition()

route.get_eq_dist_slopes(avg_slope_distance = 10)
route.integrated_slope_plot()

route.get_slopes()
route.simple_slope_plot()

auguste = cl.cyclist(weight = 76, name = "Auguste")

edict = auguste.cycle_traject_cv(route, cv = 35)

df = pd.DataFrame.from_dict(edict, orient='columns')
df2 = df.filter(regex = 'E')
df_cs = df2.cumsum()
df_cs.plot(x = np.cumsum(route.distances), y = df_cs.columns)
route.slope_plot_on_current_axis()
plt.show()

wh.get_winddata_lat_long(start[0], start[1])
wh.get_detailed_forecast_lat_long(start[0], start[1])

print("DONE")
