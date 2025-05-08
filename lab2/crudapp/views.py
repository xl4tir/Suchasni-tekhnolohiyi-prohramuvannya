from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Orders

def orderFormView(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'crudapp/order.html', {'form': form})

def showView(request):
    obj = Orders.objects.all()
    return render(request, 'crudapp/show.html', {'obj': obj})

def updateView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    form = OrderForm(instance=obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'crudapp/order.html', {'form': form})

def deleteView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'crudapp/confirmation.html', {'obj': obj})
