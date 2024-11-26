from django import forms
class ContactForm(forms.Form):
    
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone', required=False)
    message = forms.CharField(label='Mensagem',widget=forms.Textarea)

    # Certifique-se de que o `save()` está funcionando
    def save(self, commit=True):
        contact = super().save(commit=False)
        # Adicione lógica extra aqui, se necessário
        if commit:
            contact.save()
        return contact