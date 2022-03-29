from django.test import TestCase
from sms.models import Order

# Create your tests here.

class OrderTest(TestCase):
    def test_welcome(self):
        oOrder = Order(phone="519-226-1234", data = {"state":"WELCOMING"})
        aReturn = oOrder.handleInput("hello")
        print(aReturn)
        self.assertTrue("welcome" in aReturn[0].lower())
