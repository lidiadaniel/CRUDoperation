
from django.shortcuts import render,redirect
from .models import quadrilateral
from .forms import UserForm
# Create your views here.

def user_list(request):
    records=quadrilateral.objects.all()
    mydict={'records':records}
    return render(request,'table.html',context=mydict)

def AddUser(request):
    mydict={}
    form=UserForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    mydict['form']=form
    return render(request,'create.html',mydict)

def EditUser(request,id=None):
    one_rec=quadrilateral.objects.get(pk=id)
    form=UserForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict= {'form':form}
    return render(request,'update.html',context=mydict)

def DeleteUser(request,eid=None):
    one_rec = quadrilateral.objects.get(pk=eid)
    if  request.method=="POST":
         one_rec.delete()
         return redirect('/')
    return render(request,'delete.html')

def ViewUser(request,eid=None):
    mydict={}
    one_rec = quadrilateral.objects.get(pk=eid)
    mydict['quadrilateral']=one_rec
    return render(request,'View.html',mydict)