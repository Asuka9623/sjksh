import json

filename = 'data1/eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data1/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)


all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

# mags = []
# for eq_dicts in all_eq_dicts:
#     mag = eq_dicts['properties']['mag']
#     mags.append(mag)
#
# print(mags[:10])

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:10])
print(lons[:5])
print(lats[:5])