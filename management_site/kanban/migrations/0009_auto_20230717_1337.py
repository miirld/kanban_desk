# Generated by Django 2.2 on 2023-07-17 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0008_auto_20230714_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='kanban.Column', verbose_name='Столбец'),
        ),
    ]
