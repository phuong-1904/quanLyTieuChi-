from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_admin', '0014_add_parent_event_and_child_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='progress_status',
            field=models.CharField(
                choices=[
                    ('postponed', 'Hoãn'),
                    ('over_budget', 'Vượt ngân sách'),
                    ('100', '100%'),
                    ('90', '90%'),
                    ('80', '80%'),
                    ('70', '70%'),
                    ('60', '60%'),
                    ('50', '50%'),
                    ('40', '40%'),
                    ('30', '30%'),
                    ('20', '20%'),
                    ('10', '10%'),
                ],
                default='10',
                max_length=20,
            ),
        ),
    ]
