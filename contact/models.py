from django.db import models


class ContactModel(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    message = models.TextField('mensagem')
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    response = models.TextField('resposta', max_length=600, blank=True)
    response_at = models.DateTimeField('respondido em', blank=True, null=True)
    is_response = models.BooleanField('respondido', default=False)

    class Meta:
        verbose_name_plural = 'contatos'
        verbose_name = 'contato'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name