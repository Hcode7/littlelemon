from django.shortcuts import render
from .models import *
from .forms import BookingForm
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import *
from rest_framework import filters

# Create your views here.




class MenuItemView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [filters.SearchFilter]
    search_fields  = ['id','name', 'price','description']


class MenuSingleItemView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



def home(request):
    return render(request, 'pages/home.html')

def menu(request):
    items = Menu.objects.all()
    context = {'items':items}
    return render(request, 'pages/menu.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html')


def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the reservation to the database
            form.save()

    else:
        form = BookingForm()
    return render(request, 'pages/booking.html', {'form': form})


def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''

    context = {
        'menu_item': menu_item,
    }

    return render(request, 'pages/menu_item.html', context)
