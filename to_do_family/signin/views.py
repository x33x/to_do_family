from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def signin(request):
    """
    Renders the signin page.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("username:"+username+" password:"+password)
        if user is not None:
            login(request, user)
            return redirect('mytodo')  # Redirect to dashboard or another page after successful login
        else:
            error_message = "Invalid username or password. Please try again."
    else:
        error_message = ""

    return render(request, 'signin/signin.html', {'error_message': error_message})
