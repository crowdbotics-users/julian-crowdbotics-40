from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
    ]
    context = {
        'title': 'julian-crowdbotics-40',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
