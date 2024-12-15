from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ContactModel',
            name='message',
            field=models.TextField(max_length=600, verbose_name='Mensagem'),
        ),
        migrations.AlterField(
            model_name='ContactModel',
            name='response',
            field=models.TextField(blank=True, max_length=600, verbose_name='Resposta'),
        ),
    ]