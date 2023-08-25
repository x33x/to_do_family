from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def mytodo(request):
    user = request.user
    return render(request, 'mytodo/mytodo.html', {'user': user})
