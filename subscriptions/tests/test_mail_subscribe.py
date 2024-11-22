from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="José Filipe", cpf='12345678901',
                    email='jose.filipe.gomes@aluno.riogrande.ifrs.edu.br', phone='53-12345-6789')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição!'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventif.com.br', 'jose.filipe.gomes@aluno.riogrande.ifrs.edu.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = (
            'José Filipe ',
            '12345678901',
            'jose.filipe.gomes@aluno.riogrande.ifrs.edu.br',
            '53-12345-6789'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)