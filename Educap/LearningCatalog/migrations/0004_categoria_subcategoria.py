# Generated by Django 3.2.8 on 2021-10-21 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCatalog', '0003_auto_20211019_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='SubCategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LearningCatalog.categoria'),
        ),
    ]
