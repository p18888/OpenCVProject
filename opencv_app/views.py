from django.shortcuts import render,HttpResponse

from opencv_app.finger_counter  import count_finger
from opencv_app.virtual_paint  import paint_virtual

from opencv_app.personal_trainer  import pushup_count



def index(request):    
    return render(request,"all_templates/index.html")

def finger_counts(request):
    return count_finger(request)

def draw_virtual(request):
    return paint_virtual(request)

def personal_trainer(request):
    return pushup_count(request)

def home(request):
    return render(request,"all_templates/index.html")
