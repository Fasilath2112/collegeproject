from urllib import request
from django.shortcuts import redirect, render

from collegeapp.models import reg


# Create your views here.
def display(request):
    if request.method=='POST':
        obj=reg()
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.address=request.POST.get('address')
        obj.save()
        return redirect('status')
    return render(request,'college1.html')
def status(request):
    obj=reg.objects.all()
    return render(request,'table.html',{'data':obj})
def update(request,pk):
    obj=reg.objects.get(id=pk)
    if request.method=='POST':
        obj=reg.objects.get(id=pk)
        obj.name=request.POST.get('name')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.address=request.POST.get('address')
        obj.save()
        return redirect('status')
    return render(request,'update.html',{'data':obj})
def delete(request,pk):
    obj=reg.objects.get(id=pk)
    obj.delete()
    return status(request)