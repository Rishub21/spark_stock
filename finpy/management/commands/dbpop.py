
import csv
from django.core.management.base import BaseCommand
from finpy.models import Stock
from finpy.models import test




class Command(BaseCommand):
    def handle(self, *args, **options):
        TEST = test("test1")
        TEST.save()

    
                #print line

        #print "test"
