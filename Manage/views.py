import datetime
from django.http import HttpResponse
from django.shortcuts import render
import xlsxwriter
from Manage.models import Log

from Manage.forms import VisitorForm, AddressForm
from Manage.models import Visitor, Address


# def create_excel(request):
# workbook = xlsxwriter.Workbook('Visitors.xlsx')
# worksheet


def add_visitor(request):
    if request.method == 'GET':
        return render(request, 'add_visitor.html', {'form': VisitorForm(),
                                                    'address_form': AddressForm()})
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        visitor_form = VisitorForm(request.POST)
        if address_form.is_valid() and visitor_form.is_valid():
            print('form valid')

            visitor_obj = Visitor.objects.create(first_name=visitor_form.cleaned_data.get('first_name'),
                                                 middle_name=visitor_form.cleaned_data.get('middle_name'),
                                                 last_name=visitor_form.cleaned_data.get('last_name'),
                                                 email=visitor_form.cleaned_data.get('email'),
                                                 mobile=visitor_form.cleaned_data.get('mobile'),
                                                 phone=visitor_form.cleaned_data.get('phone'),
                                                 organisation=visitor_form.cleaned_data.get('organisation'),
                                                 university=visitor_form.cleaned_data.get('university'),
                                                 designation=visitor_form.cleaned_data.get('designation'),
                                                 purpose_of_visit=visitor_form.cleaned_data.get('purpose_of_visit'))

            address_obj = Address.objects.create(building=address_form.cleaned_data.get('building'),
                                                 pin_code=address_form.cleaned_data.get('pin_code'),
                                                 street=address_form.cleaned_data.get('street'),
                                                 city=address_form.cleaned_data.get('city'),
                                                 state=address_form.cleaned_data.get('state'),
                                                 country=address_form.cleaned_data.get('country'),
                                                 visitor=visitor_obj)

            visitor_name = visitor_obj.first_name + " " + visitor_obj.last_name
            log_obj = Log.objects.create(visitor=visitor_name,
                                         date_time_of_entry=datetime.datetime.now())

            # visitor_obj.save()
            return render(request, 'add_visitor.html', {'form': VisitorForm,
                                                        'address_form': AddressForm,
                                                        'success': 'Visitor Added Successfully'})
        else:
            return HttpResponse('Form Invalid')


def show_home(request):
    if request.method == 'GET':
        return render(request, 'base.html')
    return None


def view_visitors(request):
    if request.method == 'POST':
        if request.POST.get('delete_user'):
            delete_visitor = Visitor.objects.get(pk=request.POST.get('delete_user'))
            delete_visitor.delete()
            return render(request, 'view_profile.html', {'success': 'User Deleted'})

        else:
            visitor = Visitor.objects.get(pk=request.POST.get('user_name'))
            address = Address.objects.get(visitor=visitor)
            return render(request, 'view_profile.html', {'visitor': visitor,
                                                         'address': address})
    if request.method == 'GET':
        visitors = Visitor.objects.all()
        return render(request, 'view_visitors.html', {'visitors': visitors})

