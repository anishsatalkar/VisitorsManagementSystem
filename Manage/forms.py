from django.forms import ModelForm, forms

from Manage.models import Visitor, Address


class VisitorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(VisitorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields['first_name'].widget.attrs.update({'pattern':'^[a-zA-Z]*$','onkeypress':'return isAlphabet(event)'})
        self.fields['last_name'].widget.attrs.update({'pattern':'^[a-zA-Z]*$','onkeypress':'return isAlphabet(event)'})
        self.fields['middle_name'].widget.attrs.update({'pattern':'^[a-zA-Z]*$','onkeypress':'return isAlphabet(event)'})

        self.fields['email'].widget.attrs.update({'pattern':'^[a-zA-Z]*$','onkeypress':'return isAlphabet(event)'})

        self.fields['mobile'].widget.attrs.update({'pattern':'^[a-zA-Z]*$','onkeypress':'return isNumber(event)'})
        self.fields['phone'].widget.attrs.update({'pattern':'^[a-zA-Z]*$','onkeypress':'return isNumber(event)'})


    class Meta:
        
        model = Visitor
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
