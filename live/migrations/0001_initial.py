# Generated by Django 4.2.7 on 2023-11-09 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('image', models.ImageField(upload_to='note/')),
            ],
            options={
                'verbose_name': 'Rasm',
            },
        ),
        migrations.CreateModel(
            name='TextLeft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('name_left', models.CharField(max_length=200, verbose_name='Qator nomi chap taraf')),
                ('text_left', models.CharField(max_length=200, verbose_name='Text nomi chap taraf')),
                ('link_left', models.URLField(max_length=4000, verbose_name='Link url chap taraf')),
            ],
            options={
                'verbose_name': 'Chap taraf ozgarish',
            },
        ),
        migrations.CreateModel(
            name='TextRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('name_right', models.CharField(max_length=200, verbose_name="Qator nomi o'ng taraf")),
                ('text_right', models.CharField(max_length=200, verbose_name="Text nomi o'ng taraf")),
                ('link_right', models.URLField(max_length=4000, verbose_name="Link url o'ng taraf")),
            ],
            options={
                'verbose_name': "O'ng taraf ozgarish",
            },
        ),
    ]
