from django.shortcuts import render




def main(request):
    people=[
        {"name": "Ram", "age": 30, "address": "KTM"},
        {"name": "Hari", "age": 24, "address": "BKT"},
        {"name": "Sita", "age": 45, "address": "PKR"}
    ]
    return render (request, template_name= 'temp_inheritance/home.html',     context= {"people": people})



def features(request):
    items= [
        {"name": "Laptop", "feature": "A portable computer that can be used anywhere"},
        {"name": "Mouse", "feature": "A clicking input deviceof computer"},
        {"name": "Keyboard", "feature": "An Input device with keys "}
    ]
    return render (request, template_name='temp_inheritance/features.html', context={"items": items})


def pricing(request):
    prices=[
        {"laptop":"Acer", "warranty": "1 Years", "price": "NRS 75000", "avilable": "Yes"},
        {"laptop":"Dell", "warranty": "2 Years", "price": "NRS 50000", "avilable": "Out of Stock"},
        {"laptop":"Lenevo", "warranty": "-", "price": "NRS 72000", "avilable": "Yes"},
        {"laptop":"MSI", "warranty": "6 Months", "price": "NRS 85000", "avilable": "Out Of Stock"},
        {"laptop":"Macbook", "warranty": "1 Years", "price": "NRS 105000", "avilable": "Yes"},
        {"laptop":"ASUS", "warranty": "1.5 Years", "price": "NRS 92999", "avilable": "Launching Soon"},
        {"laptop":"HP", "warranty": "-", "price": "NRS 50000", "avilable": "Only 3 Piece avilable"},
        {"laptop":"Samsung", "warranty": "3 Years", "price": "NRS 45000", "avilable": "Yes"},
    ]
    return render (request, template_name='temp_inheritance/pricing.html', context={"prices":prices})