from django import forms
from django.forms import formset_factory, widgets
from .models import Invoice
class InvoiceForm(forms.Form):
    
        # fields = ['customer', 'message']
    customer = forms.CharField(
        label='Client Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Client Name',
            'rows':1
        })
    )
    bill_title = forms.CharField(
        label='Bill Title',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Bill Title',
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
    message = forms.CharField(
        label='Service Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Description',
            'rows':1
        })
    )

    fulldescription = forms.CharField(
        label='Full Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Full Description',
            'rows':1
        })
    )

 




    service_type = forms.CharField(
        label='Service Type',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Service Type',
            'rows':1
        })
    )

    termsandconditions = forms.CharField(
        label='Terms and Conditions',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Terms and Condition',
            'rows':1
        })
    )

class LineItemForm(forms.Form):
    
    service = forms.CharField(
        label='Service/Product',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Service Name'
        })
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Enter Product Description',
            "rows":1
        })
    )
    quantity = forms.IntegerField(
        label='Qty',
        widget=forms.NumberInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Quantity'
        }) #quantity should not be less than one
    )
    rate = forms.DecimalField(
        label='Rate $',
        widget=forms.NumberInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Rate'
        })
    )
    # amount = forms.DecimalField(
    #     disabled = True,
    #     label='Amount $',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control input',
    #     })
    # )
    
LineItemFormset = formset_factory(LineItemForm, extra=1)