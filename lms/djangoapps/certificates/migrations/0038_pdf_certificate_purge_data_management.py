# Generated by Django 4.2.18 on 2025-02-20 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certificates', '0037_fix_legacy_broken_invalid_certs'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurgeReferencestoPDFCertificatesCommandConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('arguments', models.TextField(blank=True, default='', help_text="Arguments for the 'purge_references_to_pdf_certificates' management command. Specify like '--certificate_ids <id1> <id2>'")),
                ('changed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
            ],
            options={
                'verbose_name': 'purge_references_to_pdf_certificates argument',
            },
        ),
    ]
