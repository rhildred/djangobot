from django.test import TestCase
import sqlite3

# Create your tests here.

from sms.models import Order


class SMSTests(TestCase):
    def test_welcome(self):
        oOrder = Order(phone = '123-456-7890', data={"state":"WELCOMING"})
        aReturn = oOrder.handleInput("hello")
        self.assertTrue("welcome" in aReturn[0].lower())
