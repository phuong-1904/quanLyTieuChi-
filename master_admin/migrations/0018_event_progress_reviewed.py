from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_admin', '0017_event_progress_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='progress_reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
