from django.db import models

class Sites(models.Model):
    siteName = models.CharField(max_length=100)
    cellIds = models.TextField()
    siteAddress = models.TextField()
    location = models.TextField()
    siteFiles = models.FileField()
    siteConditions = models.TextField()
    siteBriaf = models.TextField()
    siteState = models.TextField()
    siteOwner = models.TextField()
    sitecity = models.TextField()
    siteProvider = models.TextField()
    sitFiberNode = models.TextField()
    

