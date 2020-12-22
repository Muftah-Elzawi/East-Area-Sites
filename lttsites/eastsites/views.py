from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Eastsites
import folium
from django.db.models import Q

# Create your views here.
def index(request):
    context = {}
    query = ''
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    
    bgzsites = getSiteWithCellId(query)
    print(bgzsites[0])
    # bgzsites = Eastsites.objects.all()
    
    tooltip = 'Click For More Info'
    if len(bgzsites[0]):
        m = folium.Map(width=600, height=300,location=[bgzsites[0][0].location[0],bgzsites[0][0].location[1]], zoom_start=7)
        for i in range(0,len(bgzsites[0])):
            folium.Marker([bgzsites[0][i].location[0], bgzsites[0][i].location[1]], popup=bgzsites[0][i].siteName).add_to(m)

    m = m._repr_html_()
    context = {'bgzsites':bgzsites[0],'MAP':m}
    return render(request, 'eastsites/index.html',context)

def city(request, cityName):
    cityName = str(cityName)
    # try:
    citySites = Eastsites.objects.filter(sitecity=cityName)
    # except Eastsites.DoesNotExist:
    #     print("no data")
    m = folium.Map(width=600, height=300,location=[citySites[0].location[0],citySites[0].location[1]], zoom_start=13)
    tooltip = 'Click For More Info'
    for i in range(0,len(citySites)):
        folium.Marker([citySites[i].location[0], citySites[i].location[1]], popup=citySites[i].siteName).add_to(m)
    m = m._repr_html_()
    context = {
        'citySites':citySites,
        'MAP':m
    }
    return render(request, "eastsites/cities.html", context)

def getSiteWithCellId(query=None):
    queryset = []
    siteCellId = Eastsites.objects.filter(cellIds__icontains = query)
    queryset.append(siteCellId)
    
    return list(set(queryset))