from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_practice.settings")

app = Celery("celery_practice")
app.conf.enable_utc = False
app.conf.update(timezone="Asia/Karachi")

app.config_from_object(settings, namespace="CELERY")

# #celeery beat
app.conf.beat_schedule = {}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
