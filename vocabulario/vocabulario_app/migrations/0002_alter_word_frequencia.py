# Generated by Django 5.1.6 on 2025-05-11 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulario_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='frequencia',
            field=models.CharField(choices=[('alta', 'alta'), ('media', 'media'), ('baixa', 'baixa')], max_length=20),
        ),
    ]
