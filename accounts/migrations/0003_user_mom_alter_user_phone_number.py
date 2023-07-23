# Generated by Django 4.2.3 on 2023-07-22 15:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_birth_date_alter_user_gender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="mom",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                blank=True,
                help_text="010-XXXX-XXXX 혹은 010XXXXXXXX 모두 가능",
                max_length=13,
                validators=[
                    django.core.validators.RegexValidator("^010-?[1-9]\\d{3}-?\\d{4}$")
                ],
            ),
        ),
    ]