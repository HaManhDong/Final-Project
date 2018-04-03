# Generated by Django 2.0.3 on 2018-04-02 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('time_stamp', models.DateTimeField(primary_key=True, serialize=False, verbose_name='Time member in/out')),
                ('value', models.IntegerField(verbose_name='0/1 - out/in')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('name', models.TextField(verbose_name='member name')),
                ('email', models.EmailField(max_length=254)),
                ('card_id', models.TextField(verbose_name='card id')),
                ('course', models.TextField(null=True, verbose_name='course')),
                ('registered_day', models.DateField(auto_now_add=True)),
                ('latest_image', models.ImageField(null=True, upload_to='')),
                ('avatar', models.ImageField(null=True, upload_to='')),
                ('recognize_label', models.AutoField(primary_key=True, serialize=False)),
                ('research_about', models.TextField(null=True, verbose_name='research')),
            ],
        ),
        migrations.AddField(
            model_name='logs',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pas.Member'),
        ),
    ]