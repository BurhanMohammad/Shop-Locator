from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop
from .forms import ShopForm
from django.db.models import Q
from geopy import distance

def create_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_list')
    else:
        form = ShopForm()
    return render(request, 'shop/create_shop.html', {'form': form})

def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {'shops': shops})

def update_shop(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_list')
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop/update_shop.html', {'form': form})

def shop_within_distance(request):
    if request.method == 'POST':
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        distance_km = float(request.POST.get('distance'))
        user_location = (latitude, longitude)
        shops_within_distance = []
        shops = Shop.objects.all()
        for shop in shops:
            shop_location = (shop.latitude, shop.longitude)
            shop_distance = distance.distance(user_location, shop_location).km
            if shop_distance <= distance_km:
                shops_within_distance.append(shop)
        return render(request, 'shop/shop_within_distance.html', {'shops': shops_within_distance})
    else:
        return render(request, 'shop/shop_within_distance_form.html')
