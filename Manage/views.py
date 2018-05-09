from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Manage.forms import VisitorForm, AddressForm
from Manage.models import Visitor, Address


@login_required(login_url='/')
def add_visitor(request):
    if request.method == 'GET':
        return render(request, 'add_visitor.html', {'form': VisitorForm,
                                                    'address_form': AddressForm})
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        visitor_form = VisitorForm(request.POST)
        if address_form.is_valid() and visitor_form.is_valid():
            print('form valid')

            country_code = request.POST['country_code']
            mobile_no = visitor_form.cleaned_data.get('mobile')
            mobile_no = country_code + '-' + mobile_no

            if request.POST.get('edit_id'):
                visitor_id = request.POST.get('edit_id')
                visitor_obj = Visitor.objects.get(pk=visitor_id)

                visitor_obj.first_name = visitor_form.cleaned_data.get('first_name')
                visitor_obj.middle_name = visitor_form.cleaned_data.get('middle_name')
                visitor_obj.last_name = visitor_form.cleaned_data.get('last_name')
                visitor_obj.email = visitor_form.cleaned_data.get('email')
                visitor_obj.mobile = mobile_no
                visitor_obj.phone = visitor_form.cleaned_data.get('phone')
                visitor_obj.organisation = visitor_form.cleaned_data.get('organisation')
                visitor_obj.university = visitor_form.cleaned_data.get('university')
                visitor_obj.designation = visitor_form.cleaned_data.get('designation')
                visitor_obj.purpose_of_visit = visitor_form.cleaned_data.get('purpose_of_visit')
                visitor_obj.save()

                address = Address.objects.get(visitor=visitor_obj)
                address.building = address_form.cleaned_data.get('building')
                address.pin_code = address_form.cleaned_data.get('pin_code')
                address.street = address_form.cleaned_data.get('street')
                address.city = address_form.cleaned_data.get('city')
                address.state = address_form.cleaned_data.get('state')
                address.country = address_form.cleaned_data.get('country')
                address.save()

            else:
                visitor_obj = Visitor.objects.create(first_name=visitor_form.cleaned_data.get('first_name'),
                                                     middle_name=visitor_form.cleaned_data.get('middle_name'),
                                                     last_name=visitor_form.cleaned_data.get('last_name'),
                                                     email=visitor_form.cleaned_data.get('email'),
                                                     mobile=mobile_no,
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
            return render(request, 'add_visitor.html', {'form': VisitorForm,
                                                        'address_form': AddressForm,
                                                        'success': 'Visitor Added Successfully'})
        else:
            return HttpResponse('Form Invalid')


def show_home(request):
    if request.method == 'GET':
        return render(request, 'base.html')
    return None


@login_required(login_url='/')
def view_visitors(request):
    if request.method == 'GET':
        visitors = Visitor.objects.all()
        return render(request, 'view_visitors.html', {'visitors': visitors})


def view_profile(request):
    if request.method == 'POST':
        visitor = Visitor.objects.get(pk=request.POST.get('user_name'))
        address = Address.objects.get(visitor=visitor)
        return render(request, 'view_profile.html', {'visitor': visitor,
                                                     'address': address})
    else:
        return HttpResponseRedirect('/home/add_visitor/', {'error': 'Redirected to Home.'})


def delete_visitor(request):
    if request.method == 'POST':
        # if request.POST.get('delete_user'):
            delete_vis = Visitor.objects.get(pk=request.POST.get('delete_user'))
            delete_vis.delete()
            return render(request, 'view_profile.html', {'success': 'User Deleted'})
        # elif request.POST.get('edit_user'):
        #     return render(request, 'add_visitor.html', {'form': VisitorForm(request.POST.get('edit_user')),
        #                                                 'present_id': request.POST.get('edit_user'),
        #                                                 'address_form': AddressForm(request.POST.get('edit_user'))})
    else:
        return HttpResponseRedirect('/home/add_visitor/', {'error': 'Redirected to Home.'})


def search_visitor(request):
    if request.method == 'POST':
        query = str(request.POST.get('query'))
        only_univ = False
        only_org = False
        if request.POST.get('search'):
            if request.POST.get('search') == 'university':
                only_univ = True
            else:
                only_org = True
        visitors_to_send = []
        completed_visitors = []

        for field in Visitor._meta.fields:
            field_name = str(field).split('.')[2] + '__icontains'
            if not field_name.__contains__('date'):
                visitors = Visitor.objects.filter(**{field_name: query}).exclude(pk__in=completed_visitors)

                if visitors:
                    for visitor in visitors:
                        if only_univ:
                            if visitor.university is None:
                                continue
                        elif only_org:
                            if visitor.organisation is None:
                                continue

                        visitors_to_send.append(visitor)
                        completed_visitors.append(visitor.pk)

        for field in Address._meta.fields:
            field_name = str(field).split('.')[2] + '__icontains'
            if not field_name.__contains__('visitor'):
                addresses = Address.objects.filter(**{field_name: query}).exclude(visitor__pk__in=completed_visitors)
                if addresses:
                    for address in addresses:
                        if only_univ:
                            if address.visitor.university is None:
                                continue
                        elif only_org:
                            if address.visitor.organisation is None:
                                continue
                        visitors_to_send.append(address.visitor)
                        completed_visitors.append(address.visitor.pk)
        return render(request, 'view_visitors.html', {'returned_visitors': visitors_to_send})
    else:
        return HttpResponseRedirect('/home/view_visitors/', {'visitors': Visitor.objects.all()})


def edit_visitor(request):
    if request.method == 'POST':
        visitor_pk = request.POST.get('pk')
        visitor = Visitor.objects.get(pk=visitor_pk)
        address = Address.objects.get(visitor=visitor)
        return render(request, 'add_visitor.html', {'form': VisitorForm(instance=visitor),
                                                    'address_form': AddressForm(instance=address),
                                                    'present_id': visitor_pk})
    else:
        return HttpResponseRedirect('/home/add_visitor/', {'error': 'Redirected to Home.'})
