from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from contact.forms import ContactForm
from django.core import mail
from contact.models import ContactModel

def contact(request):
    if request.method == 'POST':
       return create(request)
    else:
        return new(request)


def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contacts/contact_form.html', {'form': form})
    
    ContactModel.objects.create(**form.cleaned_data)

    _send_mail(
        'contacts/contact_email.txt',
        form.cleaned_data,
        'Novo Contato!',
        settings.DEFAULT_FROM_EMAIL,
        form.cleaned_data['email'])

    messages.success(request, 'Envio realizado com sucesso!')
    return HttpResponseRedirect('/contato/')

    
def new(request):
    return render(request, 'contacts/contact_form.html', {'form': ContactForm()})


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o objeto no banco de dados
            return redirect('/contato/')  # Redireciona após salvar
    else:
        form = ContactForm()

    return render(request, 'contacts/contact_form.html', {'form': form})