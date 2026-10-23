from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Coffee",price="3.5",inventory=60)
        itemstr = str(item)

        self.assertEqual(itemstr, "Coffee:3.5")

class MenuViewSet(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Coffee",price="3.5",inventory=60)
        MenuItem.objects.create(title="Pizza",price="8.0",inventory=20)
        MenuItem.objects.create(title="Taco",price="1.5",inventory=15)

    def test_getall(self):
        menu_items = MenuItem.objects.all()    

        self.assertEqual(menu_items.count(),3)
        self.assertEqual(sorted(item.title for item in menu_items),["Coffee","Pizza","Taco"])


