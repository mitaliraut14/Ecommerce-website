# Generated by Django 4.1.5 on 2023-01-30 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0007_delete_recommendation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.product')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.user')),
            ],
        ),
    ]