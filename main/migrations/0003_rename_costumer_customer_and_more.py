# Generated by Django 4.1.3 on 2022-11-29 00:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_orderitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Costumer',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='custumer',
            new_name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('E', 'Em espera'), ('A', 'Aceito'), ('R', 'Rejeitado')], default='E', max_length=1),
        ),
    ]