from django.shortcuts import render, get_object_or_404
from .models import TaxDeclaration
from django.contrib.auth.decorators import login_required

def dashboard(request, pk):
    declaration = TaxDeclaration.objects.get(id=pk)

    context = {'declaration': declaration}
    return render(request, "dashboard/index.html", context)

@login_required
def taxes(request):
    declaration = TaxDeclaration.objects.filter(user=request.user)

    context = {'declaration': declaration}

    return render(request, 'dashboard/taxes.html', context)
