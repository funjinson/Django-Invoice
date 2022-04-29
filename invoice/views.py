from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template.loader import get_template
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib import messages
from django.views import View
from .models import LineItem1, Invoice1, LineItem2, Invoice2
from .forms import LineItemFormset1, InvoiceForm1, LineItemFormset2, InvoiceForm2
from django.template import loader
from django.contrib.auth.decorators import login_required

import pdfkit
import csv

class InvoiceListView2(View):

    def get(self, *args, **kwargs):
        invoices2 = Invoice2.objects.all().order_by('-id')
        context = {

            "invoices2": invoices2,
        }

        return render(self.request, 'invoice/invoice-list-2.html', context)


    def post(self, request):
        # import pdb;pdb.set_trace()
        invoice2_ids = request.POST.getlist("invoice2_id")
        invoice2_ids = list(map(int, invoice2_ids))

        invoices2 = Invoice2.objects.filter(id__in=invoice2_ids)
        # import pdb;pdb.set_trace()

        return redirect('invoice:invoice-list-2')


class InvoiceListView1(View):
    def get(self, *args, **kwargs):
        invoices1 = Invoice1.objects.all().order_by('-id')
        context = {
            "invoices1": invoices1,
        }

        return render(self.request, 'invoice/invoice-list.html', context)

    def post(self, request):
        # import pdb;pdb.set_trace()
        invoice1_ids = request.POST.getlist("invoice2_id")
        invoice1_ids = list(map(int, invoice1_ids))

        invoices1 = Invoice1.objects.filter(id__in=invoice1_ids)
        # import pdb;pdb.set_trace()

        return redirect('invoice:invoice-list')


def createInvoice1(request):
    """
    Invoice Generator page it will have Functionality to create new invoices, 
    this will be protected view, only admin has the authority to read and make
    changes here.
    """

    heading_message = 'Apro IT Solutions'
    if request.method == 'GET':
        formset = LineItemFormset1(request.GET or None)
        form = InvoiceForm1(request.GET or None)
    elif request.method == 'POST':
        formset = LineItemFormset1(request.POST)
        form = InvoiceForm1(request.POST)

        gstpercentageinfloat = form.data["gst"]
        a = float(gstpercentageinfloat) * 100
        b = int(a)
        servicea = form.data["service"]
        


        if servicea == 'https://www.aprorigs.com/wp-content/uploads/2021/11/logo3.png':
            terms1 = form.data["termsandconditionsaprorigs"]
            additionalnotes = form.data["fulldescriptionrigs"]

        elif servicea == 'https://aproitsolutions.com/wp-content/uploads/2019/07/apro-logo-for-web-new-dark-1.png':
            terms1 = form.data["termsandconditionsaproitsolutions"]
            additionalnotes = form.data["fulldescriptionit"]

        elif servicea == 'https://aprohosting.com/wp-content/uploads/2021/11/logo-02.png':
            terms1 = form.data["termsandconditionsaprohosting"]
            additionalnotes = form.data["fulldescriptionaprohosting"]

        else:
            terms1 = form.data["termsandconditionsaprocms"]
            additionalnotes = form.data["fulldescriptioncms"]


        currencycountry = form.data["currency"]
        footerdefault = form.data["footer"]

        if form.is_valid():
            invoice1 = Invoice1.objects.create(customer=form.data["customer"],
                                               bill_title=form.data["bill_title"],
                                               gst=gstpercentageinfloat,
                                               termsandconditions=terms1,
                                               fulldescription=additionalnotes,
                                               date=form.data["date"],
                                               service_type=form.data["service_type"],
                                               gstpercentage=b,
                                               service=servicea,
                                               currency=currencycountry,
                                               footer=footerdefault

                                               )

            # invoice.save()

        if formset.is_valid():
            # import pdb;pdb.set_trace()
            # extract name and other data from each form and save
            total = 0

            for form in formset:
                service = form.cleaned_data.get('service')
                description = form.cleaned_data.get('description')
                quantity = form.cleaned_data.get('quantity')
                rate = form.cleaned_data.get('rate')

                if service and description and quantity and rate:
                    amount = float(rate) * float(quantity)

                    total += amount
                    LineItem1(customer=invoice1,
                              service=service,
                              description=description,
                              quantity=quantity,
                              rate=rate,
                              amount=amount).save()
            invoice1.total_amount = total
            totala = float(total)
            gsta = float(gstpercentageinfloat)
            gsttotala = totala * gsta
            floata = gsttotala
            format_float = "{:.2f}".format(floata)

            invoice1.gsttotal = format_float
            subtotal = gsttotala + totala
            abc = float(subtotal)
            invoice1.subtotal = abc
            invoice1.save()

            try:
                generate_PDF1(request, id=invoice1.id)
            except Exception as e:
                print(f"********{e}********")
            return redirect('/')
    context = {
        "title": "Invoice Generator",
        "formset": formset,
        "form": form,
    }
    return render(request, 'invoice/invoice-create.html', context)

def createInvoice2(request):
    """
    Invoice Generator page it will have Functionality to create new invoices,
    this will be protected view, only admin has the authority to read and make
    changes here.
    """

    heading_message = 'Apro IT Solutions'
    if request.method == 'GET':
        formset = LineItemFormset2(request.GET or None)
        form = InvoiceForm2(request.GET or None)
    elif request.method == 'POST':
        formset = LineItemFormset2(request.POST)
        form = InvoiceForm2(request.POST)

        gstpercentageinfloat = form.data["gst"]
        a = float(gstpercentageinfloat) * 100
        b = int(a)

        servicea = form.data["service"]



        if servicea == 'https://www.aprorigs.com/wp-content/uploads/2021/11/logo3.png':
            terms1 = form.data["termsandconditionsaprorigs"]
            additionalnotes = form.data["fulldescriptionrigs"]

        elif servicea == 'https://aproitsolutions.com/wp-content/uploads/2019/07/apro-logo-for-web-new-dark-1.png':
            terms1 = form.data["termsandconditionsaproitsolutions"]
            additionalnotes = form.data["fulldescriptionit"]

        elif servicea == 'https://aprohosting.com/wp-content/uploads/2021/11/logo-02.png':
            terms1 = form.data["termsandconditionsaprohosting"]
            additionalnotes = form.data["fulldescriptionaprohosting"]

        else:
            terms1 = form.data["termsandconditionsaprocms"]
            additionalnotes = form.data["fulldescriptioncms"]


        currencycountry = form.data["currency"]
        footerdefault = form.data["footer"]

        if form.is_valid():
            invoice2 = Invoice2.objects.create(customer=form.data["customer"],
                                               bill_title=form.data["bill_title"],
                                               gst=gstpercentageinfloat,
                                               termsandconditions=terms1,
                                               fulldescription=additionalnotes,
                                               date=form.data["date"],
                                               service_type=form.data["service_type"],
                                               gstpercentage=b,
                                               service=servicea,
                                               currency=currencycountry,
                                               footer=footerdefault

                                               )

            # invoice.save()

        if formset.is_valid():
            # import pdb;pdb.set_trace()
            # extract name and other data from each form and save
            total = 0

            for form in formset:
                service = form.cleaned_data.get('service')
                description = form.cleaned_data.get('description')
                quantity = form.cleaned_data.get('quantity')
                rate = form.cleaned_data.get('rate')

                if service and description and quantity and rate:
                    amount = float(rate) * float(quantity)

                    total += amount
                    LineItem2(customer=invoice2,
                              service=service,
                              description=description,
                              quantity=quantity,
                              rate=rate,
                              amount=amount).save()
            invoice2.total_amount = total
            totala = float(total)
            gsta = float(gstpercentageinfloat)
            gsttotala = totala * gsta
            floata = gsttotala
            format_float = "{:.2f}".format(floata)

            invoice2.gsttotal = format_float
            subtotal = gsttotala + totala
            abc = float(subtotal)
            invoice2.subtotal = abc
            invoice2.save()

            try:
                generate_PDF2(request, id=invoice2.id)
            except Exception as e:
                print(f"********{e}********")
            return redirect('/')
    context = {
        "title": "Invoice Generator",
        "formset": formset,
        "form": form,
    }
    return render(request, 'invoice/invoice-create-2.html', context)



def view_PDF1(request, id=None):
    invoice1 = get_object_or_404(Invoice1, id=id)
    lineitem1 = invoice1.lineitem1_set.all()

    context = {
        "company": {
            "name": "APRO IT Solutions Pvt. Ltd.",
            "address001": "2nd Floor, Supriya Building, South Junction",
            "address002": "Chalakudy, Kerala - 680307, Tel. +91 62 386 83 058",
            # "phone": "+91 9746344984",
            "website": "www.aproitsolutions.com",
            "email": "info@aproitsolutions.com",
        },
        "invoice_id": invoice1.id,
        "invoice_gst": invoice1.gst,
        "invoice_total": invoice1.total_amount,
        "customer": invoice1.customer,
        "bill_title": invoice1.bill_title,
        "fulldescription": invoice1.fulldescription,
        "termsandconditions": invoice1.termsandconditions,
        "service": invoice1.service,
        "date": invoice1.date,
        "service_type": invoice1.service_type,
        "gstpercentage": invoice1.gstpercentage,
        "subtotal": invoice1.subtotal,
        "gsttotal": invoice1.gsttotal,
        "currency": invoice1.currency,
        "lineitem1": lineitem1,
    }
    return render(request, 'invoice/pdf2oldnew.html', context)


def view_PDF2(request, id=None):
    invoice2 = get_object_or_404(Invoice2, id=id)
    lineitem2 = invoice2.lineitem2_set.all()

    context = {
        "company": {
            "name": "APRO IT Solutions Pvt. Ltd.",
            "address001": "2nd Floor, Supriya Building, South Junction",
            "address002": "Chalakudy, Kerala - 680307, Tel. +91 62 386 83 058",
            # "phone": "+91 9746344984",
            "website": "www.aproitsolutions.com",
            "email": "info@aproitsolutions.com",
        },
        "invoice_id": invoice2.id,
        "invoice_total": invoice2.total_amount,
        "customer": invoice2.customer,
        "bill_title": invoice2.bill_title,
        "fulldescription": invoice2.fulldescription,
        "termsandconditions": invoice2.termsandconditions,
        "service": invoice2.service,
        "date": invoice2.date,
        "service_type": invoice2.service_type,
        "subtotal": invoice2.subtotal,
        "currency": invoice2.currency,
        "lineitem2": lineitem2,
    }
    return render(request, 'invoice/pdfout.html', context)


def generate_PDF1(request, id):
    options = {

        'margin-top': '0.00in',
        'margin-right': '0.00in',
        'margin-bottom': '0.00in',
        'margin-left': '0.00in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip') ],

        'no-outline': None
    }

    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('invoice:invoice-detail', args=[id])), True,
                          options=options)
    response = HttpResponse(pdf, content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename="pdf.pdf"'
    return response


def generate_PDF2(request, id):
    options = {
        'page-size': 'a4',
        'margin-top': '0.00in',
        'margin-right': '0.00in',
        'margin-bottom': '0.00in',
        'margin-left': '0.00in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip') ],
        'no-outline': None
    }
    # Use False instead of output path to save pdf to a variable
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('invoice:invoice-detail', args=[id])), False,  options=options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pdf.pdf"'
    return response


def change_status1(request):
    return redirect('invoice:invoice-list')


def view_4041(request, *args, **kwargs):
    return redirect('invoice:invoice-list')


def deleteInvoice2(request, id):
    try:
        record = Invoice2.objects.get(id=id)
        record.delete()
    except:
        messages.info(request, f'The requested id doesnot exists!')
    return redirect('invoice:invoice-list-2')


def deleteInvoice1(request, id):
    try:
        record = Invoice1.objects.get(id=id)
        record.delete()
    except:
        messages.info(request, f'The requested id doesnot exists!')
    return redirect('invoice:invoice-list')


def update1(request, id):
    invoice1 = Invoice1.objects.get(id=id)
    template = loader.get_template('invoice/edittaxcustomers.html')
    context = {
        'invoice1': invoice1,
    }
    return HttpResponse(template.render(context, request))


def updaterecord1(request, id):
    customer = request.POST['customername']
    bill_title = request.POST['billtitle']
    service_type = request.POST['service_type']
    invoice1 = Invoice1.objects.get(id=id)
    invoice1.customer = customer
    invoice1.bill_title = bill_title
    invoice1.service_type = service_type
    invoice1.save()
    messages.info(request, f'The Customer {customer} has been updated successfully!')
    return redirect('/')


def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['id', 'customer', 'date', 'service_type','bill_title','total_amount','termsandconditions'])

    for customers in Invoice1.objects.all().values_list('id', 'customer', 'date', 'service_type','bill_title','total_amount','termsandconditions'):
        writer.writerow(customers)

    response['Content-Disposition'] = 'attachment; filename="members.csv"'

    return response
