from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_admin', '0018_event_progress_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='progress_review_status',
            field=models.CharField(
                choices=[
                    ('pending', 'Chờ duyệt'),
                    ('approved', 'Đã duyệt'),
                    ('rejected', 'Từ chối'),
                ],
                default='pending',
                max_length=20,
            ),
        ),
    ]
