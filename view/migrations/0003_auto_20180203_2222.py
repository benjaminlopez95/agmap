# Generated by Django 2.0.1 on 2018-02-04 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0002_auto_20180203_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='field',
            name='commodity',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.SET_NULL, to='view.Commodity'),
        ),
        migrations.AlterField(
            model_name='field',
            name='variety',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Variety',
        ),
    ]