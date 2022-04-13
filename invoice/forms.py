from django import forms
from django.forms import formset_factory, widgets
from .models import Invoice1, Invoice2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CHOICES=[('https://www.aprorigs.com/wp-content/uploads/2021/11/logo3.png','Apro Rigs'),
         ('https://aproitsolutions.com/wp-content/uploads/2019/07/apro-logo-for-web-new-dark-1.png','Apro IT Solutions'),
         ('https://t4.ftcdn.net/jpg/04/40/92/73/360_F_440927381_ljaelLw3fiAaM7baJB4kqN6BHCguhJ0l.jpg','Apro CMS')]

CURRENCY=[('₹','India'),
          ('$','USA'),
          ('د.إ','UAE')]

FOOTER=[('https://svgshare.com/i/fkr.svg','Default')]

class InvoiceForm1(forms.Form):


    service = forms.ChoiceField(
        label ='Select Service',
        choices=CHOICES,
        widget=forms.RadioSelect)

    currency = forms.ChoiceField(
        label='Select Currency',
        choices=CURRENCY,
        widget = forms.Select(attrs={
            'class': 'form-control',
        })
    )

    footer = forms.ChoiceField(
        label='Select Footer',
        choices=FOOTER,
        widget = forms.Select(attrs={
            'class': 'form-control',
        })
    )


    #fields = ['customer', 'message']
    customer = forms.CharField(max_length=50,
        label='Customer Name',
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Customer Name',
        'rows':1
        })
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={
        'type':'date'
        })

    )
    bill_title = forms.CharField(max_length=148,
        label='Bill Title',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title of Bill',
            'rows':1
        })
    )
    #billing_address = forms.CharField(
    #    label='Billing Address',
    #    widget=forms.TextInput(attrs={
    #        'class': 'form-control',
    #        'placeholder': '',
    #        'rows':1
    #    })
    #)

    # service_message = forms.CharField(max_length=34,
    #     label='Service Description',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Service Description',
    #         'rows':1
    #     })
    # )

    fulldescription = forms.CharField(
        label='Additional Notes',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Additional Notes',
            'rows':2
        })
    )
    service_type = forms.CharField(max_length=48,
        label='Service Type',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apro Rigs - Mining Rigs',
            'rows':1
        })
    )
    termsandconditions = forms.CharField(
        label='Terms and Conditions',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Terms and Conditions',
            'rows':2
        })
    )
class InvoiceForm2(forms.Form):


    service = forms.ChoiceField(
        label ='Select Service',
        choices=CHOICES,
        widget=forms.RadioSelect)

    currency = forms.ChoiceField(
        label='Select Currency',
        choices=CURRENCY,
        widget = forms.Select(attrs={
            'class': 'form-control',
        })
    )

    footer = forms.ChoiceField(
        label='Select Footer',
        choices=FOOTER,
        widget = forms.Select(attrs={
            'class': 'form-control',
        })
    )


    #fields = ['customer', 'message']
    customer = forms.CharField(max_length=50,
        label='Customer Name',
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Customer Name',
        'rows':1
        })
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={
        'type':'date'
        })

    )
    bill_title = forms.CharField(max_length=148,
        label='Bill Title',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title of Bill',
            'rows':1
        })
    )
    #billing_address = forms.CharField(
    #    label='Billing Address',
    #    widget=forms.TextInput(attrs={
    #        'class': 'form-control',
    #        'placeholder': '',
    #        'rows':1
    #    })
    #)

    # service_message = forms.CharField(max_length=34,
    #     label='Service Description',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Service Description',
    #         'rows':1
    #     })
    # )

    fulldescription = forms.CharField(
        label='Additional Notes',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Additional Notes',
            'rows':2
        })
    )
    service_type = forms.CharField(max_length=48,
        label='Service Type',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apro Rigs - Mining Rigs',
            'rows':1
        })
    )
    termsandconditions = forms.CharField(
        label='Terms and Conditions',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Terms and Conditions',
            'rows':2
        })
    )

class LineItemForm1(forms.Form):
    
    service = forms.CharField(
        label='Service/Product',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Product/Service Name'
        })
    )
    description = forms.CharField(min_length=40,
        label='Description',
        widget=forms.Textarea(attrs={
            'class': 'form-control input',
            'placeholder': 'Enter Product Description',
            "rows":1
        })
    )
    quantity = forms.IntegerField(min_value=1,
        label='Qty',
        widget=forms.NumberInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Quantity'


        }) #quantity should not be less than one
    )
    rate = forms.DecimalField(
        label='Rate',
        widget=forms.NumberInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Rate'

        })
    )
    #amount = forms.DecimalField(
       #disabled = False,
      #label='Amount $',
       #widget=forms.TextInput(attrs={
        #    'class': 'form-control input',
        #})
    #)
class LineItemForm2(forms.Form):

    service = forms.CharField(
        label='Service/Product',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Product/Service Name'
        })
    )
    description = forms.CharField(min_length=5,
        label='Description',
        widget=forms.Textarea(attrs={
            'class': 'form-control input',
            'placeholder': 'Enter Product Description',
            "rows":1
        })
    )
    quantity = forms.IntegerField(min_value=1,
        label='Qty',
        widget=forms.NumberInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Quantity'


        }) #quantity should not be less than one
    )

    # rate = forms.DecimalField(
    #     label='Rate',
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control input rate',
    #         'placeholder': 'Rate'
    #
    #     })
    # )
    amount = forms.CharField(
       disabled = False,
       label='Amount $',
       widget=forms.TextInput(attrs={
           'class': 'form-control input',
        })
    )


LineItemFormset1 = formset_factory(LineItemForm1, extra=1)
LineItemFormset2 = formset_factory(LineItemForm2, extra=1)










