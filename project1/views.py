import csv
import io
import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


from django.conf import settings
from django.shortcuts import render
from .model_selector import check_model_type
from .forms import CSVUploadForm
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Welcome to Project 1!")


def upload_csv(request):
    result = None
    error = None
    model_type = None

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            decoded_file = file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)

            try:
                column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
                df = pd.read_csv(io_string)
                df.columns = column_names
                model_type = check_model_type(df)
                print(model_type)
                # reader = csv.reader(io_string)
                # numbers = []

                # for row in reader:
                #     for item in row:
                #         try:
                #             numbers.append(float(item.strip()))
                #         except ValueError:
                #             pass  # Skip non-numeric values

                # if numbers:
                #     result = sum(numbers) / len(numbers)
                # else:
                #     error = "No numeric values found in the CSV."
            except Exception as e:
                error = f"Error processing file: {str(e)}"
    else:
        form = CSVUploadForm()
    print(model_type)
    return render(request, 'project1/upload.html', {
        'form': form,
        'result': result,
        'error': error,
        'model_type': model_type
    })