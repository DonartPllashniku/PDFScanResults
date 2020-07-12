from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
import os
import json
# Donart

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user, filename)

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filesize = models.IntegerField()
    filename = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add= True)
    document = models.FileField(upload_to=user_directory_path, max_length=200)

    def datenotime(self):
        return self.date.strftime('%B %d %Y')


@receiver(models.signals.post_delete, sender=Document)
def submission_delete(sender, instance, **kwargs):
    instance.document.delete(False)



class ScanPdf(models.Model):
    category=models.TextField(max_length=1000)
    category_value = models.IntegerField()
    document=models.ForeignKey(Document, on_delete=models.CASCADE)

    @classmethod
    def create(self, category, category_value, document):
        result = self(category=category, category_value=category_value, document=document)
        return result

    def __str__(self):
        return str(self.category)

class Results(models.Model):
    prediction = models.IntegerField()
    document=models.ForeignKey(Document, on_delete=models.CASCADE)

    @classmethod
    def create(self, prediction, document):
     
        result = self(prediction=prediction, document=document)
        return result

    def __str__(self):
        return str(self.prediction)


class InformationExtracted(models.Model):
    information = models.TextField(max_length=100000)
    result = models.ForeignKey(Results, on_delete=models.CASCADE)
    # prediction = models.IntegerField(choices=Labels.choices)


    @classmethod
    def create(self, information, result):
        result = self(information=information, result=result)
        return result

