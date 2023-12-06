from django.shortcuts import render
from . import ner_model


from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages






def index(request):
    return render(request, 'index.html')

def model(request):
    return render(request, 'model.html')

def about(request):
    return render(request, 'about.html')

def api(request):
    return render(request, 'api.html')


def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def header(request):
    return render(request, 'header.html')


def analyze_text(request):
    if request.method == 'POST':
        # Extract the text input from the form
        text = request.POST.get('text')

        # Load the spaCy model
        nlp = ner_model.load_model()

        # Process the text using the loaded model
        doc = nlp(text)

        # Extract the entities from the processed document
        entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]

        # Prepare the context for rendering the template
        context = {'text': text, 'entities': entities}

        return render(request, 'result.html', context)

    return render(request, 'model.html')


