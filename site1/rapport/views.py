from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def presentation(request):
    return render(request, 'presentation.html')

def deroulement(request):
    return render(request, 'deroul.html')

def description(request):
    return render(request, 'description-metier.html')

def conditions(request):
    return render(request, 'conditions.html')

def merci(request):
    return render(request, 'merci.html')

def conclusion(request):
    return render(request, 'conclusion.html')

from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import render

@xframe_options_exempt
def typescript_doc(request):
    return render(request, 'typescript.html')

@xframe_options_exempt
def mysqldoc(request):
    return render(request, 'mysql-doc.html')

@xframe_options_exempt
def htmldoc(request):
    return render(request, 'html-doc.html')

@xframe_options_exempt
def cssdoc(request):
    return render(request, 'css-doc.html')

@xframe_options_exempt
def phpdoc(request):
    return render(request, 'php-doc.html')

@xframe_options_exempt
def debaindoc(request):
    return render(request, 'linux-tuto.html')

@xframe_options_exempt
def glpidoc(request):
    return render(request, 'glpi-tuto.html')

@xframe_options_exempt
def axisdoc(request):
    return render(request, 'axis.html')