# Generated by Django 3.2.6 on 2021-10-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_externaldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ausschreibungen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nummer', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('Status', models.CharField(max_length=200)),
                ('Auftraggeber', models.CharField(max_length=200)),
                ('Region', models.CharField(max_length=200)),
                ('Auftragswert', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Beguenstigter', models.CharField(max_length=200)),
                ('DatumNotifikation', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='externaldata',
            name='Mitarbeiter_ID',
            field=models.CharField(max_length=200),
        ),
    ]