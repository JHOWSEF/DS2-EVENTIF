from django.contrib import admin
from django.db.models.signals import pre_save
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.dispatch import receiver
from django.utils.timezone import now
from django.conf import settings
from contact.models import ContactModel
from datetime import datetime
from decouple import config

class ContactModelAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'phone', 'message', 'created_at', 'response', 'response_at', 'is_response', 'response_today'
    )
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'message', 'created_at', 'response', 'is_response')
    list_filter = ('response',)

    def response_today(self, obj):
        
        if obj.response_at: 
           return obj.response_at.date() == now().date()
        return False  

    response_today.short_description = 'Respondido hoje?'
    response_today.boolean = True


@receiver(pre_save, sender=ContactModel)
def send_email_response(sender, instance, **kwargs):
    
    if instance.pk:  
        old_instance = ContactModel.objects.filter(pk=instance.pk).first()
    else:
        old_instance = None

    # Verifica se 'response' foi adicionado ou alterado
    if instance.response and (not old_instance or old_instance.response != instance.response):
        subject = "Resposta do seu contato com o Eventif"
        
        body = render_to_string('contacts/contact_response.txt', {
            'name': instance.name,
            'phone': instance.phone,
            'email': instance.email,
            'message': instance.message,
            'response': instance.response,
        })
        to_emails = [
            instance.email,  # Email do usuário
            settings.DEFAULT_FROM_EMAIL  # Email do eventif
        ]
        
        send_mail(
            subject,  # Assunto
            body,  # Corpo do e-mail renderizado
            config('EMAIL_HOST_USER'),  # Email remetente (do arquivo .env)
            to_emails,  # Lista de destinatários
            fail_silently=False,
        )
        
admin.site.register(ContactModel, ContactModelAdmin)