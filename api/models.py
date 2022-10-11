from django.db import models



class House(models.Model):
    image = models.FileField(upload_to='images', null=True, blank=True)
    rent_price = models.IntegerField(default=0)
    house_size = models.TextField(max_length=500)
    location = models.TextField(max_length=500)
    bedroom = models.IntegerField(default=0)
    bathroom = models.IntegerField(default=0)
    house_name = models.TextField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.house_name


class Img(models.Model):
    images = models.FileField(upload_to='imgs')
    house = models.ForeignKey(House, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return str(self.house)
