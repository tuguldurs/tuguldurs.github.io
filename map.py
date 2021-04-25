import getorg
from geopy import Nominatim as gpN

m = getorg.orgmap.create_map_obj()
gc = gpN(user_agent='x')

with open('map.dat') as f:
    lines = f.readlines()
    locs = [line.strip() for line in lines]

locdict = {}
for loc in locs: locdict[loc] = gc.geocode(loc)

for loc in locs:
    if locdict[loc] == None: print(f'fix ---> {loc}')

getorg.orgmap.output_html_cluster_map(locdict, hashed_usernames=False)
