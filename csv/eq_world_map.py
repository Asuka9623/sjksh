import plotly.express as px
import json
import  pandas as pd

filename = 'data1/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

mags, titles, lons, lats = [], [], [], []
all_eq_dicts = all_eq_data['features']
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['精度', '维度', '位置', '震极']
)
data.head()

fig = px.scatter(
    data,
    x=lons,
    y=lats,
    labels={'x': '经度', 'y':'纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震极',
    size_max=10,
    color='震极',
    hover_name='位置',
)
fig.write_html('global_earthquakes.html')
fig.show()