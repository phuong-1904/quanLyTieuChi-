from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_admin', '0016_alter_event_progress_status_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='progress_reason',
            field=models.TextField(blank=True, default=''),
        ),
    ]
