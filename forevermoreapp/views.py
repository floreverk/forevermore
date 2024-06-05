from django.shortcuts import render
import folium
import pandas as pd

list = ['naam', 'lon', 'lat', 'marker']

# Create your views here.
def home(request):
    df = pd.read_excel(r"C:\Users\flore.verkest\Documents\Documenten\code\forevermore\forevermore\forevermoreapp\static\data\forevermore.xlsx")
    
    m = folium.Map(location=[50.849086622118364, 2.877732908267023], zoom_start=12,)
    for naam in df['naam']:
        df_01 = df[df['naam']==naam]
        lon = df_01['lon'].iloc[0]
        lat = df_01['lat'].iloc[0]
        marker = df_01['marker'].iloc[0]
        tooltip = "Click me!"
        marker = folium.Marker(
            [lon, lat],
            popup=marker,
            tooltip=tooltip
        )
        marker.add_to(m)
    
    map = m._repr_html_()
    context = {
      'map': map,

    }
    return render(request, 'home.html', context)

def AbeeleAerodromeMilitaryCemetery(request):
    df = pd.read_excel(r"C:\Users\flore.verkest\Documents\Documenten\code\forevermore\forevermore\forevermoreapp\static\data\images.xlsx")
    df_01 = df[df['naam']=='Abeele Aerodrome Military Cemetery']
    naam = df_01['naam'].iloc[0]
    image_list = []
    for objectnummer in df_01['objectnummer']:
        bestandsnaam = objectnummer + ".jpg"
        pad = 'images/' + bestandsnaam
        image_list.append(pad)
    context = {'image_list': image_list, 'naam':naam}
    return render(request, 'plaats.html', context)

def AeroplaneCemetery(request):
    df = pd.read_excel(r"C:\Users\flore.verkest\Documents\Documenten\code\forevermore\forevermore\forevermoreapp\static\data\images.xlsx")
    df_01 = df[df['naam']=='Aeroplane Cemetery']
    naam = df_01['naam'].iloc[0]
    image_list = []
    for objectnummer in df_01['objectnummer']:
        bestandsnaam = objectnummer + ".jpg"
        pad = 'images/' + bestandsnaam
        image_list.append(pad)
    context = {'image_list': image_list, 'naam':naam}
    return render(request, 'plaats.html', context)

def AdinkerkeMilitaryCemetery(request):
    df = pd.read_excel(r"C:\Users\flore.verkest\Documents\Documenten\code\forevermore\forevermore\forevermoreapp\static\data\images.xlsx")
    df_01 = df[df['naam']=='Adinkerke Military Cemetery']
    naam = df_01['naam'].iloc[0]
    image_list = []
    for objectnummer in df_01['objectnummer']:
        bestandsnaam = objectnummer + ".jpg"
        pad = 'images/' + bestandsnaam
        image_list.append(pad)
    context = {'image_list': image_list, 'naam':naam}
    return render(request, 'plaats.html', context)

def AncreBritishCemetery (request):
    df = pd.read_excel(r"C:\Users\flore.verkest\Documents\Documenten\code\forevermore\forevermore\forevermoreapp\static\data\images.xlsx")
    df_01 = df[df['naam']=='Ancre British Cemetery ']
    naam = df_01['naam'].iloc[0]
    image_list = []
    for objectnummer in df_01['objectnummer']:
        bestandsnaam = objectnummer + ".jpg"
        pad = 'images/' + bestandsnaam
        image_list.append(pad)
    context = {'image_list': image_list, 'naam':naam}
    return render(request, 'plaats.html', context)

