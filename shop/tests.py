from django.test import TestCase, Client
from django.urls import reverse
from .models import Shop
from .forms import ShopForm

class ShopTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.shop1 = Shop.objects.create(name="Shop 1", latitude=16.516822, longitude=80.637201, address="123 Main St.", description="A great shop")
        self.shop2 = Shop.objects.create(name="Shop 2", latitude=16.515873, longitude=80.663862, address="456 Elm St.", description="Another great shop")

    def test_shop_creation(self):
        form_data = {'name': 'New Shop', 'latitude': 16.516822, 'longitude': 80.637201, 'address': '789 Oak St.', 'description': 'A new shop'}
        form = ShopForm(data=form_data)
        self.assertTrue(form.is_valid())
        shop = form.save()
        self.assertEqual(shop.name, 'New Shop')
        self.assertEqual(shop.latitude, 16.516822)
        self.assertEqual(shop.longitude, 80.637201)
        self.assertEqual(shop.address, '789 Oak St.')
        self.assertEqual(shop.description, 'A new shop')

    def test_shop_list_view(self):
        response = self.client.get(reverse('shop_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shop 1")
        self.assertContains(response, "Shop 2")

    def test_shop_update_view(self):
        url = reverse('shop_update', args=[self.shop1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shop 1")
        form_data = {'name': 'Updated Shop', 'latitude': 16.516822, 'longitude': 80.637201, 'address': '321 Pine St.', 'description': 'An updated shop'}
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('shop_list'))
        updated_shop = Shop.objects.get(id=self.shop1.id)
        self.assertEqual(updated_shop.name, 'Updated Shop')
        self.assertEqual(updated_shop.latitude, 16.516822)
        self.assertEqual(updated_shop.longitude, 80.637201)
        self.assertEqual(updated_shop.address, '321 Pine St.')
        self.assertEqual(updated_shop.description, 'An updated shop')

    def test_shop_within_distance_view(self):
        response = self.client.get(reverse('shop_within_distance'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shops Within Distance")
        form_data = {'latitude': 16.516822, 'longitude': 80.637201, 'distance': 1}
        response = self.client.post(reverse('shop_within_distance'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Shop 1")
        self.assertNotContains(response, "Shop 2")
