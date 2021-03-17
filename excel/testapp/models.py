from django.db import models

# Create your models here.
class abhyudaya(models.Model):
    BANKNAME = models.CharField(max_length = 100)
    IFSC     = models.CharField(max_length = 100)
    OFFICE   = models.CharField(max_length = 100)
    ADDRESS  = models.CharField(max_length = 200)

class ahmedabad(models.Model):
    BANKNAME = models.CharField(max_length = 100)
    IFSC     = models.CharField(max_length = 100)
    OFFICE   = models.CharField(max_length = 100)
    ADDRESS  = models.CharField(max_length = 200)
