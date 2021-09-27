# Generated by Django 3.2.7 on 2021-09-23 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Bank name')),
                ('int_rate', models.IntegerField(verbose_name='Interest rate')),
                ('max_loan', models.IntegerField(verbose_name='Max loan')),
                ('min_dep', models.IntegerField(verbose_name='Minimum down payment')),
                ('loan_term', models.IntegerField(verbose_name='Loan term')),
            ],
        ),
    ]
