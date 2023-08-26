from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.hashers import make_password

def signup(request):
    """
    Renders the signup page.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            sign_up = form.save(commit=False)
            print('Before make_pass')
            print(sign_up)
            sign_up.password = make_password(form.cleaned_data['password'])
            print('After make_pass')
            print(sign_up)
            sign_up.save() # Save the form data to the database
            return redirect('signin')  # Redirect to the signin page after successful signup
            print('Signup successfully created')
    else:
        form = SignupForm()

    return render(request, 'signup/signup.html', {'form': form})
