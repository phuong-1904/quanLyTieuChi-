from django.db import migrations


def sync_progress_review_status(apps, schema_editor):
    Event = apps.get_model('master_admin', 'Event')
    Event.objects.filter(
        progress_reviewed=True,
        progress_review_status='pending',
    ).update(progress_review_status='approved')


class Migration(migrations.Migration):

    dependencies = [
        ('master_admin', '0019_event_progress_review_status'),
    ]

    operations = [
        migrations.RunPython(sync_progress_review_status, migrations.RunPython.noop),
    ]
