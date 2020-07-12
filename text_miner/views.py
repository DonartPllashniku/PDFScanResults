# pylint: disable=E1101 
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.template.loader import get_template
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from PDFMining.settings import *
import json


import backend.using_model
import os
import re


from django.core.files.storage import FileSystemStorage
from .models import Document, ScanPdf, Results
from .forms import DocumentForm
from backend.using_model import predictResult


from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 4

# Donart
from backend.preparation.PdfIdUser import my_method

# Create your views here.
from django.http import HttpResponse
def check_for_authentication(request, path):
    if not request.session.has_key('username'):
        return redirect("../")
    else:
        return render(request, path, {})


def generate_view(request, *args, **kwargs):
    long_version = "False"
    if(request.GET['long'] != None):
        long_version=request.GET['long']

    if long_version!="True":       
        template = get_template('html2pdf.html')
        results = Results.objects.all().filter(document=request.GET["docid"])
        context = {
            'results':results,
            'doc_name': request.GET['docname']
        }
        html = template.render(context)
        pdf = render_to_pdf('html2pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Result_%s.pdf" %(request.GET['docname'])
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
    elif long_version=="True":
        template = get_template('pdf_result_long.html')
        results = Results.objects.all().filter(document=request.GET["docid"])
        context = {
            'results':results,
            'doc_name': request.GET['docname']
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf_result_long.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Result_%s_Long.pdf" %(request.GET['docname'])
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
    
    return HttpResponse("Not found")

def upload_viewer(request):
    files = Document.objects.all().filter(user_id=request.user)
    return render(request, 'viewer.html', {
        "files": files
    })

def del_uploaded(request):
    docs=Document.objects.all()
    docs.delete()
    return redirect('../')

def del_file(request,pk):
    if request.method=="POST":
       doc=Document.objects.get(pk=pk)
       doc.delete()
    return redirect('../')



def base(request,*args,**kwargs):
    if request.session.has_key('username'):
        return render(request, 'base.html')
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        request.session['username'] = username

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("textminer/")
        else:
            return render(request, 'sign-in.html', {})
    else:
        return render(request, 'sign-in.html', {})

@xframe_options_exempt
def pdfviewer(request):
    with open('static/assets/Gothaer Leistungstexte kurz.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=some_file.pdf'
        return response

@xframe_options_exempt
def pdfview(request):
    return render(request, "viewer.html", {})


def logout(request):
    auth.logout(request)
    try:
        del request.session['username']

    except:
     pass
    return redirect("../")

#TODO change this technique with a better one to handle logout
def logout2(request):
    auth.logout(request)
    try:
        del request.session['username']
    except:
     pass
    return redirect("../../")

def textminer(request,*args,**kwargs):
    if not request.session.has_key('username'):
        return redirect("../")
    else:
        if request.method == 'POST' and request.is_ajax():
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                instance = Document(document=request.FILES['document'])
                instance.user = request.user
                filename_uploaded=request.FILES['document'].name
                filename_uploaded = re.sub(", ", "_", filename_uploaded)
                filename_uploaded = re.sub(",", "_", filename_uploaded)
                filename_uploaded = re.sub(" ", "_", filename_uploaded)
                instance.filename=filename_uploaded
                sizeb=int(request.FILES['document'].size)
                sizekb=sizeb/1024
                instance.filesize=sizekb
                instance.save()

                docs = Document.objects.all().filter(user_id=request.user)
                docs = docs[len(docs)-1]
                doc_id = docs._meta.get_field("id")
                doc_id_value = doc_id.value_from_object(docs)
                doc_name = docs._meta.get_field("filename")
                doc_name_value = doc_name.value_from_object(docs)

                field_object = docs._meta.get_field("filename")
                field_value = field_object.value_from_object(docs)
                doc_path = 'media\\user_{0}\\{1}'.format(request.user, field_value)
                file_path = os.path.join(BASE_DIR, doc_path)
                
                lista_name, lista_values = my_method(doc_path)

                # temp_list = list()
                # result_dict = list()
                # temp_list = list()
                # res = Results.objects.all().filter(document=  doc_id_value)
                # temp_list.append(res[0].prediction)
                # temp_list.append(docs.filename)
                # temp_list.append(docs.id)
                # result_dict.append(temp_list)
                # print(result_dict)

                for index, res in enumerate(lista_name):
                    res_saved=ScanPdf.create(res, lista_values[index], docs)
                    res_saved.save()
                
                prediction_result = predictResult(lista_values) 
                res_saved=Results.create(prediction_result,  docs)
                res_saved.save()
                if(prediction_result==0):
                    prediction_result_value="Nothing harmful has been founded in this document!"
                else:
                    prediction_result_value="This document may be harmful to your Device!"
                print("LIRI")
                print(prediction_result_value)

         
                return JsonResponse({'error': False, 'message': 'Uploaded Successfully',  "doc_name": doc_name_value, "doc_id": doc_id_value, "doc_result_text": prediction_result_value})
            else:
                return JsonResponse({'error': True, 'errors': form.errors})
        else:
            form = DocumentForm()

        docs = Document.objects.all().filter(user_id=request.user)
        results=None
        doc_name_value=""
        doc_id_value=""

       
        
        # categories = Categories.objects.all()
        # keywords = Keywords.objects.all()


        
        return render(request,"base.html", {
            'form': form,
            'results':results,
            'doc_name':doc_name_value,
            'doc_id':doc_id_value,
            
        })

def documents(request,*args,**kwargs):
    if not request.session.has_key('username'):
        return redirect("../")
    else:
        resultsd=[]
        docindex=[]
        docs = Document.objects.all().filter(user_id=request.user)
        for index, doc in enumerate(docs):
            docindex.append([index,doc])
            results = Results.objects.all().filter(user_id=request.user, document_id=doc.id)
            resultsd.append(results)
        return render(request, 'documents.html', {
            "docindex": docindex,
            "resultsd":resultsd
        })

def mcheck(request,*args,**kwargs):

    if not request.session.has_key('username'):
        return redirect("../")
    

# Donart Rezultati qe kthehet ne html
    else:
        docs = Document.objects.all().filter(user_id=request.user)
        temp_list = list()
        result_dict = list()
        for i in docs:
            temp_list = list()
            res = Results.objects.all().filter(document= i)
            temp_list.append(res[0].prediction)
            temp_list.append(i.filename)
            temp_list.append(i.id)
            result_dict.append(temp_list)
        print(result_dict)
        
        # categories = Categories.objects.all()
        # keywords = Keywords.objects.all()
        results = None
        return render(request, "mcheck.html", {
            "docs":docs,
            "result_dict": result_dict
            # "user:": request.user,
            # "categories": categories,
            # "keywords": keywords
            })

# def about(request,*args,**kwargs):
#     return check_for_authentication(request,"about.html")

# def contact(request,*args,**kwargs):
#     return check_for_authentication(request,"contact.html")

def search(request):
    return render(request, 'search.json', {})



#USE THIS METHOD TE RECREATE THE DATABASE --- CALL URL /create_database
def create_database(request):
    from backend.queries.categories import fill_categories, fill_keywords
    fill_categories()
    fill_keywords()
    return HttpResponse("Success - Check terminal")