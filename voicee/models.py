from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.language

class Website(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Auteur(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name