import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])#loading elevation data into python list

def color_producer(elevation):#used for dynamic elevation colours
    if elevation<1000:
        return 'green' #return type is string
    elif 1000<= elevation <3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Toner")

#We can add objects to the elements to the map before saving it.
fgv=folium.FeatureGroup(name="Volcanos")#use to add multiple features like polygon etc and also to keep organise n add layer control features

for lt,ln,el in zip(lat,lon,elev): #when we use two lists at the same time we have to use zip function.It takes first item of first list and first item of second list at the same time
#the below method is referred to as children                     #fillcolor is to fill the inner area  #outter ring for perimeter we are using grey color as outline
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6,popup=str(el)+" m b",
    fill_color=color_producer(el),color='grey',fill=True,fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")

                            #open is used to open the file from where and read it here.
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<= x['properties']['POP2005']<20000000 else 'red'}))#geojson is aspecial case of json/its starts with curly braces. It is similar to python dictionary with keys and values.


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())#add layer control after featuregroup object is being added because it will be just a plain default map.

map.save("Map1.html")
