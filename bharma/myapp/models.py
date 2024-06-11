from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="userImage")
    date = models.DateTimeField(auto_now_add=True)



# from django.db import models

# class Image(models.Model):
#     photo = models.ImageField(upload_to="userImage")
#     date = models.DateTimeField(auto_now_add=True)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
