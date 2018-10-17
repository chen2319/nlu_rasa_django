from django.shortcuts import render
from django.http import HttpResponse
import train.train_nlu_data as tn


# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def train(request):
    tn.train_data();
    return HttpResponse("NLU data trained.")