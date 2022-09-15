from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
    return render(request, "wishlist.html", context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request):
    return HttpResponse(serializers.serialize("xml", data2), content_type="application/json")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request):
    return HttpResponse(serializers.serialize("json", data2), content_type="application/json")

data = BarangWishlist.objects.all()

data2 = BarangWishlist.objects.filter(pk=1)

data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Nadhif Rahman Alfan Ganteng Mantap Betul Onde Mande Cool'
}

