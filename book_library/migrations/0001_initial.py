# Generated by Django 4.0.1 on 2022-02-03 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=60)),
                ('taken', models.BooleanField(default=True, verbose_name='В наличии')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_library.author')),
                ('co_author', models.ManyToManyField(blank=True, related_name='Соавтор', to='book_library.Author', verbose_name='Соавторы')),
                ('reader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='book_library.reader')),
            ],
            options={
                'verbose_name': 'Книгу',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
