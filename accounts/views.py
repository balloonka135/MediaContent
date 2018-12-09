from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


class SignUpFormView(CreateView):
    '''
    Class-based view for User Sign Up form.
    '''
    success_url = reverse_lazy('login')
    form_class = forms.UserForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        form.save()
        return super(SignUpFormView, self).form_valid(form)
