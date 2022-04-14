from multiprocessing import context
from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import ImageForm

def index(request):
    return redirect('uploader_page:upload')

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance to display in the template
            img_obj = form.instance
            return render(request, 'uploader_page/index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'uploader_page/index.html', {'form': form})