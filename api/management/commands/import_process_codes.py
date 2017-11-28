from django.core.management.base import BaseCommand
from api.models import ProcessCode
import csv

class Command(BaseCommand):
    help = 'Import ICD10 codes'

    def handle(self, *args, **options):

        with open('data/process/dh_rate_dieticians.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                code = ProcessCode()
                code.practice_type_code = row[0]
                code.name = row[1]
                code.description = row[2]
                code.discovery_rate = row[3]
                code.save()

            print ('Imported: {} codes'.format(ProcessCode.objects.count()))