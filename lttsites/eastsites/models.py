from django.db import models

# Create your models here.
class Eastsites(models.Model):
    siteName = models.CharField(max_length=100)
    cellIds = models.JSONField()
    siteAddress = models.TextField()
    location = models.JSONField()
    siteFiles = models.FileField()
    siteConditions = models.TextField()
    siteBriaf = models.TextField()
    siteState = models.TextField()
    siteOwner = models.TextField()
    sitecity = models.TextField()
    siteProvider = models.TextField()
    sitFiberNode = models.TextField()