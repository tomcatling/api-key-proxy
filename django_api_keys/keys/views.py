#views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404

from .models import *
from .forms import *
 
# Create your views here.


@login_required
def index(request):
    internal_keys = InternalKey.objects.filter(owner=request.user)
 
    form = InternalKeyForm()
 
    if request.method == 'POST':
        form = InternalKeyForm(request.POST)
        if form.is_valid():
            internal_key = form.save(commit=False)
            internal_key.owner = request.user
            internal_key.save()
        return redirect('/')
 
    context = {'internal_keys': internal_keys, 'form': form}
    return render(request, 'internal_key/list.html', context)
 
 
@login_required
def updatingInternalKey(request, pk):
    internal_key = InternalKey.objects.get(id=pk)
 
    form = InternalKeyForm(instance=internal_key)
 
    if request.method == 'POST':
        form = InternalKeyForm(request.POST, instance=internal_key)
        if form.is_valid():
            form.save()
            return redirect('/')
 
    context = {'form': form}
 
    return render(request, 'internal_key/update.html', context)

@login_required
def deleteInternalKey(request, pk):
    item = InternalKey.objects.get(id=pk)
 
    if request.method == 'POST':
        item.delete()
        return redirect('/')
 
    context = {'item': item}
 
    return render(request, 'internal_key/delete.html', context)

