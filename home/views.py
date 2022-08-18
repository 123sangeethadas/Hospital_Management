from django.http import HttpResponse
from django.shortcuts import render
from .models import Department, Doctors

from .forms import BookingForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def department(request):
    dict_dept = {
        'depnt': Department.objects.all()
    }

    return render(request, 'Department.html', dict_dept)


def booking(request, ):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()


    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)


def doctor(request):
    dict_doctor = {
        'doctors': Doctors.objects.all()
    }

    return render(request, 'doctor.html', dict_doctor)


def contact(request):
    return render(request, 'contact.html')
