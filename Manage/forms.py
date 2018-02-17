from django.forms import ModelForm, Textarea, DateTimeInput, forms, DateInput
from django import forms

from Manage.models import Visitor, Address


class DateInputOne(forms.DateTimeInput):
    input_type = 'datetime'


class VisitorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(VisitorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['first_name'].widget.attrs.update(
            {'pattern': '^[a-zA-Z ]*$', 'onkeypress': 'return isAlphabet(event)'})
        self.fields['last_name'].widget.attrs.update(
            {'pattern': '^[a-zA-Z ]*$', 'onkeypress': 'return isAlphabet(event)'})
        self.fields['middle_name'].widget.attrs.update(
            {'pattern': '^[a-zA-Z ]*$', 'onkeypress': 'return isAlphabet(event)'})

        self.fields['mobile'].widget.attrs.update({'pattern': '^[a-zA-Z+]*$', 'onkeypress': 'return isNumber(event)'})
        self.fields['phone'].widget.attrs.update({'pattern': '^[a-zA-Z+]*$', 'onkeypress': 'return isNumber(event)'})

        # self.fields['date_time_of_entry'].widget.attrs.update({'pattern': '^[a-zA-Z+]*$', 'onkeypress': 'return isNumber(event)'})

    class Meta:
        model = Visitor
        widgets = {
            'purpose_of_visit': Textarea(attrs={'cols': '10', 'rows': '5'}),
            # 'begin_start_date': DateTimeInput(format='DATETIME_FORMAT', attrs={
            #     'id': 'dateField', 'class': 'form-control date'}),
            'date_time_of_entry': DateTimeInput(attrs={'id':'datepicker1','class':'date'})
        }
        fields = '__all__'


class AddressForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['pin_code'].widget.attrs.update({'pattern': '^[a-zA-Z]*$', 'onkeypress': 'return isNumber(event)'})

    class Meta:
        model = Address
        fields = '__all__'
        exclude = ['visitor']
