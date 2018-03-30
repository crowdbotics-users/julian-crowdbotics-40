from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-twitter-api', 'url': 'http://pypi.python.org/pypi/django-twitter-api/0.2.10'},
	{'name':'django-twitter-bootstrap', 'url': 'http://pypi.python.org/pypi/django-twitter-bootstrap/3.3.0'},
    ]
    context = {
        'title': 'julian-crowdbotics-40',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
