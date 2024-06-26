# Generated by Django 4.2.6 on 2023-11-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_alter_produto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promocional'),
        ),
    ]
