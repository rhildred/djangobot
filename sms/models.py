from django.db import models

# Create your models here.

class Order(models.Model):
    phone = models.CharField(max_length=255, default='')
    data = models.JSONField()
    def handleInput(self, sInput):
        aReturn = []
        sState = self.data["state"]
        if sState == "WELCOMING":
            aReturn.append("Welcome to Rich's Rapid Test.")
            aReturn.append("Would you like to reserve a rapid test kit?")
            self.data["state"] = "RESERVING"
        elif sState == "RESERVING":
            self.data["reserved"] = sInput.lower()
            self.data["state"] = "DONE"
            if sInput.lower()[0]  == 'y':
                aReturn.append("Your rapid test is reserved under the phone number " +  self.phone)
            else:
                aReturn.append("Thanks for trying our reservation system")
                aReturn.append("Maybe next time")
             
        return aReturn
    def isDone(self):
        if self.data["state"] == "DONE":
            return True
        else:
            return False