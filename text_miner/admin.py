from django.contrib import admin
# Donart
# Register your models here.
from .models import Document, ScanPdf,Results

admin.site.register(ScanPdf)
admin.site.register(Document)
admin.site.register(Results)