from django.test import TestCase
from django.core import mail
from django.core.mail import send_mail
from contact.forms import ContactForm
from contact.models import ContactModel

class ContactGet(TestCase):

    def setUp(self):
        self.response = self.client.get('/contato/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.response, 'contacts/contact_form.html')

    def test_html(self):
        tags = (
            ('<form', 1),
            ('<input', 5),
            ('type="text"', 2),
            ('type="email"',1),
            ('type="submit"',1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')




class ContactPostValid(TestCase):
    
    def setUp(self):
        self.data = {
            'name': 'José Filipe',
            'email': 'jfmarques0909.shadow@gmail.com',
            'phone':'53-12345-6789',
            'message': 'Mensagem de teste'
        }
        # Simula um POST para a URL de contato
        self.resp = self.client.post('/contato/', self.data)

    def test_post(self):
        self.assertRedirects(self.resp, '/contato/')

    def test_send_contact_email(self):
        self.assertEqual(1, len(mail.outbox))
    
    def test_save_contact(self):
        self.assertFalse(ContactModel.objects.exists())



class ContactPostInvalid(TestCase):

    def setUp(self):
        self.resp = self.client.post('/contato/', {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'contacts/contact_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_form_has_error(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)



class ContactEmailPostValid(TestCase):

    def setUp(self):
        data = dict(name="José Filipe", email='jfmarques0909.shadow@gmail.com', phone='53-12345-6789',
        message='mensagem teste')
        self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = 'Novo Contato!'
        self.assertEqual(expect, self.email.subject)

    def test_contact_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ['contato@eventif.com.br', 'jfmarques0909.shadow@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = (
            'José Filipe',
            'jfmarques0909.shadow@gmail.com',
            '53-12345-6789',
            'mensagem teste'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)