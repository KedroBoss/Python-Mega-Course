import folium
import pandas

df = pandas.read_csv('Volcanoes-USA.txt')

map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start = 4, tiles = 'Stamen Terrain')

def elev_to_color(elev):
    col = ''
    minv = int(min(df['ELEV']))
    step = int((max(df['ELEV'])-min(df['ELEV']))/3)
    if elev in range(minv, minv+step):
        col = 'green'
    elif elev in range(minv, minv+step*2):
        col = 'orange'
    else:
        col = 'red'
    return col



fg = folium.FeatureGroup(name='Volcano')


for lat, lon, nam, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    fg.add_child(folium.Marker(location=[lat, lon],popup = "Volcano "+nam, icon = folium.Icon(color = elev_to_color(elev), icon_color = 'green')))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('WorldPop.json'),
name='World Population',
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(folium.LayerControl())
map.save('test.html')
