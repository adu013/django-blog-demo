from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(
        request,
        template_name='accounts/signup.html',
        context=context
    )


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:article_list')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(
        request,
        template_name='accounts/login.html',
        context=context
    )


def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:article_list')
