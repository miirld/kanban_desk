# Generated by Django 2.2 on 2023-07-19 19:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0011_auto_20230718_1639'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='column',
            name='unique position',
        ),
        migrations.AlterField(
            model_name='card',
            name='position',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='column',
            name='position',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Позиция'),
        ),
        migrations.AddConstraint(
            model_name='card',
            constraint=models.UniqueConstraint(fields=('column', 'position'), name='unique card position'),
        ),
        migrations.AddConstraint(
            model_name='column',
            constraint=models.UniqueConstraint(fields=('board', 'position'), name='unique column position'),
        ),
    ]
