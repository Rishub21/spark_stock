from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backtester.settings') # this will point celery to the settings that we need it for
app = Celery('backtester') # creating instance of celery library in our project


app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) # allows us to automatically see if there is a task.pt file with thigns that we need to execute

"""
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
"""
