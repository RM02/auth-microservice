# Generated by Django 4.2.2 on 2023-08-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_managers_alter_user_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(auto_created=True, default='bcrypt_sha256$$2b$12$9jCXeepalK9cWj2jeDJNnOTm34s2ycpG438ymuHLfZ.zV2oMVFPQq', max_length=250),
        ),
    ]