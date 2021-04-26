from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request): 
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(request, 'first_app/index.html', context=date_dict)

def webpage_name(request): 
    webpages_list = Webpage.objects.order_by('name')
    webpage_dict = {'webpage_records': webpages_list}
    return render(request, 'first_app/second.html', context=webpage_dict)