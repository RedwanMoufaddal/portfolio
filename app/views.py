from django.shortcuts import render
from .models import Base, Services,Project
# Create your views here.
def home(request):
    info = Base.objects.get(my_gmail="ridouanmoufaddal1@gmail.com")
    serv = Services.objects.all()
    pro = Project.objects.all()
    return render(request, 'index.html',{'info':info,'serv':serv,'pro':pro})