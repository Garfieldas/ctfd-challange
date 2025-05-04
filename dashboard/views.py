from django.shortcuts import render, get_object_or_404
from .models import TaxDeclaration

def dashboard(request, pk):
    declaration = TaxDeclaration.objects.get(id=pk)

    context = {'declaration': declaration}
    return render(request, "dashboard/index.html", context)

def taxes(request):
    declaration = TaxDeclaration.objects.filter(user=request.user)

    context = {'declaration': declaration}

    return render(request, 'dashboard/taxes.html', context)
