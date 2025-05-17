import csv
import io
import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


from django.conf import settings
from django.shortcuts import render
from .utils import DataInvestigator
from .forms import CSVUploadForm
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Welcome to Project 1!")

def upload_csv(request):
    result = None
    error = None
 
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            decoded_file = file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
        
            try:
                df = pd.read_csv(io_string)
                investigator = DataInvestigator(df)  
                result = investigator.perform_analysis()

            except Exception as e:
                error = f"Error processing file: {str(e)}"
    else:
        form = CSVUploadForm()

    if result is not None:

        return render(request, 'project1/upload.html', {
            'model_recommendation': result["Model Recommendation"],
            'dataset_summary': result["Dataset Summary"][1],
            'plot': result["Data Analyser"],
            'form': form,
            'error': error
        })

    return render(request, 'project1/upload.html', {
            'form': form,
            'error': error
        })