import os
import pandas as pd
import numpy as np
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import shutil

def index(request):
    # Путь к Excel-файлу
    file_path = os.path.join(settings.BASE_DIR, 'data', 'table.xlsx')

    try:
        # Читаем первый лист Excel
        df = pd.read_excel(file_path)
        
        # Заменяем "unnamed" и "nan" на пустые значения
        df = df.replace(to_replace=[r'(?i)^Unnamed.*', np.nan], value='', regex=True)
        
        # Преобразуем в список списков (заголовки + строки)
        table_data = [df.columns.tolist()] + df.values.tolist()
    except Exception as e:
        table_data = []
        print(f"Ошибка при чтении файла: {e}")

    return render(request, 'index.html', {'table': table_data})

@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        # Получаем расширение файла
        file_extension = os.path.splitext(uploaded_file.name)[1]
        
        # Формируем путь для сохранения файла
        file_path = os.path.join(settings.BASE_DIR, 'data', f'table{file_extension}')
        
        # Сохраняем файл
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        return HttpResponse("Файл успешно загружен и сохранен как table" + file_extension)
    
    return render(request, 'admin_upload.html')