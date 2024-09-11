from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, CustomerLocation



def add_customer(request):
    if request.method == "POST":
        customer = Customer.objects.create(
            customer_title_name=request.POST['customer_title_name'],
            customer_name=request.POST['customer_name'],
            customer_nickname=request.POST['customer_nickname'],
            customer_phone=request.POST['customer_phone'],
            customer_email=request.POST.get('customer_email', ''),
        )

        CustomerLocation.objects.create(
            customer=customer,
            customer_province=request.POST['customer_province'],
            customer_district=request.POST['customer_district'],
            customer_canton=request.POST['customer_canton'],
            customer_postal_number=request.POST['customer_postal_number'],
            customer_house_number=request.POST['customer_house_number'],
        )

        return redirect('customer_list')

    return render(request, 'register.html')


def customer_list(request):
    customers = Customer.objects.prefetch_related('customerlocation_set').all()
    return render(request, 'preview.html', {'customers': customers})



def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    location = customer.customerlocation_set.first()

    if request.method == "POST":
        customer.customer_title_name = request.POST['customer_title_name']
        customer.customer_name = request.POST['customer_name']
        customer.customer_nickname = request.POST['customer_nickname']
        customer.customer_phone = request.POST['customer_phone']
        customer.customer_email = request.POST.get('customer_email', '')
        customer.save()

        location.customer_province = request.POST['customer_province']
        location.customer_district = request.POST['customer_district']
        location.customer_canton = request.POST['customer_canton']
        location.customer_postal_number = request.POST['customer_postal_number']
        location.customer_house_number = request.POST['customer_house_number']
        location.save()

        return redirect('customer_list')

    return render(request, 'edit_customer.html', {'customer': customer, 'location': location})



def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return redirect('customer_list')