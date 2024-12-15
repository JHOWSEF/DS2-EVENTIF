from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('phone', models.CharField(max_length=20, verbose_name='telefone')),
                ('message', models.TextField(verbose_name='mensagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('response', models.TextField(blank=True, max_length=600, verbose_name='resposta')),
                ('response_at', models.DateTimeField(blank=True, null=True, verbose_name='respondido em')),
                ('is_response', models.BooleanField(default=False, verbose_name='respondido')),
            ],
            options={
                'verbose_name': 'contato',
                'verbose_name_plural': 'contatos',
                'ordering': ('-created_at',),
            },
        ),
    ]
