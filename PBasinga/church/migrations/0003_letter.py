# Generated by Django 4.2.4 on 2024-03-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0002_conversation_utalk_delete_message_delete_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=2000)),
                ('message', models.CharField(max_length=2000000)),
            ],
        ),
    ]
