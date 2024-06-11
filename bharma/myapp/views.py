from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.

def home(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 return render(request, 'myapp/home.html', {'img':img, 'form':form})



# from django.shortcuts import render
# from .forms import ImageForm
# from .models import Image

# def home(request):
    # if request.method == "POST":
    #     form = ImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         # Save the form data to get the instance
    #         instance = form.save(commit=False)
            
    #         # Get latitude and longitude data
    #         latitude = request.POST.get('latitude')
    #         longitude = request.POST.get('longitude')

    #         # Assign latitude and longitude to the instance
    #         instance.latitude = latitude
    #         instance.longitude = longitude

    #         # Save the instance with latitude and longitude
    #         instance.save()

    # form = ImageForm()
    # img = Image.objects.all()
    # return render(request, 'myapp/home.html', {'img':img, 'form':form})



# from django.shortcuts import render
from django.http import HttpResponse

def volunteer_registration(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        # Process volunteer registration (e.g., save to database)
        # Example:
        # Volunteer.objects.create(name=name, email=email, phone=phone, address=address)
        
        # Redirect to a thank you page or home page
        return HttpResponse('Thank you for registering as a volunteer!')

    # If not a POST request, render the form template
    return render(request, 'volunteer_registration.html')

# def resources_view(request):
#     # Your view logic goes here
#     return render(request, 'resources.html')