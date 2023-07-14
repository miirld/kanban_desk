# Generated by Django 2.2 on 2023-07-14 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0005_column'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.CharField(blank=True, max_length=300, verbose_name='Описание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно?')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='Позиция')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cards', to='kanban.Column', verbose_name='Столбец')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['position'],
            },
        ),
    ]
