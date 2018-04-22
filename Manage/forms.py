from django.forms import ModelForm, Textarea, DateTimeInput, forms, DateInput, Select
from django import forms
from Manage.models import Visitor, Address
import json


class VisitorForm(ModelForm):
    model = Visitor

    CHOICES = []
    with open('data.json') as data_file:
        from_json = json.load(data_file)

    for i in range(0, len(from_json['countries'])):
        # pprint(from_json['countries'][i])
        # print((str(from_json['countries'][i]['name']), from_json['countries'][i]['code']))
        CHOICES.append((str('+' + from_json['countries'][i]['code']),
                        (str(from_json['countries'][i]['full']) + " +" + from_json['countries'][i]['code'])))

    # print(CHOICES)
    country_code = forms.ChoiceField(choices=CHOICES)

    def __init__(self,*args,  **kwargs):
        super(VisitorForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        # if id != "":
        #     visitor = Visitor.objects.get(pk=id)
        #     self.fields['first_name'].widget.attrs.update(
        #         {'value': visitor.first_name}
        #     )
        #
        #     self.fields['middle_name'].widget.attrs.update(
        #         {'value': visitor.middle_name}
        #     )
        #
        #     self.fields['last_name'].widget.attrs.update(
        #         {'value': visitor.last_name}
        #     )
        #
        #     self.fields['first_name'].widget.attrs.update(
        #         {'value': visitor.first_name}
        #     )
        #
        #     self.fields['email'].widget.attrs.update(
        #         {'value': visitor.email}
        #     )
        #
        #     self.fields['mobile'].widget.attrs.update(
        #         {'value': visitor.mobile}
        #     )
        #
        #     self.fields['phone'].widget.attrs.update(
        #         {'value': visitor.phone}
        #     )
        #
        #     self.fields['organisation'].widget.attrs.update(
        #         {'value': visitor.organisation}
        #     )
        #
        #     self.fields['university'].widget.attrs.update(
        #         {'value': visitor.university}
        #     )
        #
        #     self.fields['designation'].widget.attrs.update(
        #         {'value': visitor.designation}
        #     )
        #
        #     self.fields['date_time_of_entry'].widget.attrs.update(
        #         {'value': visitor.date_time_of_entry}
        #     )
        #
        #     self.fields['purpose_of_visit'].widget.attrs.update(
        #         {'value': visitor.purpose_of_visit}
        #     )

        self.fields['first_name'].widget.attrs.update(
            {'pattern': '^[a-zA-Z ]*$', 'id': 'first_name_field'})
        self.fields['last_name'].widget.attrs.update(
            {'pattern': '^[a-zA-Z ]*$'})
        self.fields['middle_name'].widget.attrs.update(
            {'pattern': '^[a-zA-Z ]*$'})

        # ,'pattern': '^[a-zA-Z+]*$'
        self.fields['mobile'].widget.attrs.update({'id': 'mobile_field', 'onkeypress': 'return isNumber(event)'})
        self.fields['phone'].widget.attrs.update({'id': 'phone_field', 'onkeypress': 'return isNumber(event)'})

    class Meta:

        model = Visitor

        widgets = {

            'purpose_of_visit': Textarea(attrs={'cols': '10', 'rows': '5'}),

            'date_time_of_entry': DateTimeInput(attrs={'id': 'datepicker1', 'class': 'date'})
        }
        fields = '__all__'


class AddressForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        # if id != "":
        #     visitor = Visitor.objects.get(pk=id)
        #     address = Address.objects.get(visitor=visitor)
        #     self.fields['building'].widget.attrs.update(
        #         {'value': address.building}
        #     )
        #
        #     self.fields['pin_code'].widget.attrs.update(
        #         {'value': address.pin_code}
        #     )
        #
        #     self.fields['street'].widget.attrs.update(
        #         {'value': address.street}
        #     )
        #
        #     self.fields['city'].widget.attrs.update(
        #         {'value': address.city}
        #     )
        #
        #     self.fields['state'].widget.attrs.update(
        #         {'value': address.state}
        #     )
        #
        #     self.fields['country'].widget.attrs.update(
        #         {'value': address.country}
        #     )

        self.fields['pin_code'].widget.attrs.update(
            {'id': 'pin_code_field', 'pattern': '^[a-zA-Z]*$', 'onkeypress': 'return isNumber(event)'})

    class Meta:
        model = Address
        fields = '__all__'
        exclude = ['visitor']
