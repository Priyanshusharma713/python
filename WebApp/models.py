from django.db import models
import datetime
# Create your models here.


class UserModel(models.Model):
    name=models.CharField(max_length=20)
    contact=models.CharField(max_length=10)
    entry_time=models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name + "" + str(self.id)
    
class product(models.Model):
    prod_img=models.ImageField(upload_to="procucts_images/")
    desxription=models.TextField(max_length=160)
    price=models.CharField(max_length=6)
    