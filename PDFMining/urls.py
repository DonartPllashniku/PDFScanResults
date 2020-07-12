"""PDFMining URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from text_miner.views import base, mcheck,del_file, logout, logout2, textminer, pdfviewer, generate_view, pdfview, documents, del_uploaded, create_database, search # ,get_ajax, testing
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('about/',about),
    # path('contact/',contact),
    path('textminer/',textminer),
    path('delete/', del_uploaded),
    path('documents/', documents),
    path('documents/<int:pk>/', del_file, name='del_file'),
    path('pdf/', pdfviewer),
    path('pdfview/', pdfview),
    path('mcheck/', mcheck),
    path('',base),
    path('logout/',logout),
    path('mcheck/logout/',logout2),
    path('about/logout/',logout2),
    path('contact/logout/',logout2),
    path('textminer/logout/',logout2),
    path('documents/logout/',logout2),
    # path('get_ajax',get_ajax),
    path('Results/',generate_view),
    # path('testing/', testing), 
    path('create_database/', create_database),
    path('assets/data/search.json', search)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
