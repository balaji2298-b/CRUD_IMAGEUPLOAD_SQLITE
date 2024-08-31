from django.shortcuts import render,redirect
from myapp.models import Blue
from django.contrib import messages
import os

def index(request):
	blues = Blue.objects.all()
	context = {'blues':blues}
	return render(request,'index.html',context)

def create(request):
	if request.method == "POST":
		blue = Blue()
		blue.name = request.POST.get('name')
		blue.phonenumber = request.POST.get('phonenumber')
		blue.email = request.POST.get('email')

		if len(request.FILES) != 0:
			blue.image = request.FILES['image']
		blue.save()
		messages.success(request,"New Member Successfully Added")
		return redirect('/')
	return render(request, 'index.html')

def edit(request, id):
	blue = Blue.objects.get(id=id)
	if request.method == "POST":
		if len(request.FILES) != 0:
			if len(blue.image) > 0:
				os.remove(blue.image.path)
			blue.image = request.FILES['image']
		blue.name = request.POST.get('name')
		blue.phonenumber = request.POST.get('phonenumber')
		blue.email = request.POST.get('email')
		blue.save()
		messages.success(request, "Updated Successfully")
		return redirect('/')
	context = {'blue':blue }
	return render(request, 'edit.html', context)

def delete(request, id):
	blue = Blue.objects.get(id=id)
	if len(blue.image) > 0:
		os.remove(blue.image.path)
	blue.delete()
	messages.success(request,"Deleted Successfully")
	return redirect('/')
	




















# def create(request):
# 	blue = Blue(name=request.POST['name'], phonenumber=request.POST['phonenumber'], email=request.POST['email'], image=request.POST['image'])
# 	blue.save()
# 	return redirect('/')

# def read(request):
# 	blues = Blue.objects.all()
# 	context = {'blues': blues}
# 	return render(request, 'result.html', context)

# def edit(request,id):
# 	blues = Blue.objects.get(id=id)
# 	context = {'blue': blues}
# 	return render(request,'edit.html', context)

# def update(request,id):
# 	blue = Blue.objects.get(id=id)
# 	blue.name = request.POST['name']
# 	blue.phonenumber = request.POST['phonenumber']
# 	blue.email = request.POST['email']
# 	blue.image = request.POST['image']
# 	blue.save()
# 	return redirect('/')

# def delete(request,id):
# 	blue = Blue.objects.get(id=id)
# 	blue.delete()
# 	return redirect('/')




