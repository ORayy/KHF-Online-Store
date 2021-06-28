from django.shortcuts import render

# Create your views here.

# view function for basket summary page
def basket_summary(request):
    return render(request, 'khfApp/basket/summary.html')