from django.core.management.base import BaseCommand
from api.models import ProcessCode
import csv

class Command(BaseCommand):
    help = 'Import ICD10 codes'

    def handle(self, *args, **options):

        [p.delete() for p in ProcessCode.objects.all()]
        files = [
            'dh_rate_bio.csv',
            'dh_rate_dieticians.csv',
            'dh_rate_psychology.csv',
            'dh_rate_chiropractor2.csv',
            'dh_rate_dieticians2.csv',
            'dh_rate_speech_therapy_and_audiology.csv',
            #'dh_rate_consult_code.csv',
            'dh_rate_occupational_therapy.csv',
            #'dh_rate_dental_guide.csv',
            'dh_rate_podiatry.csv',
        ]
        for file in files:
            with open('data/process/dh_rate_dieticians.csv') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    code = ProcessCode()
                    code.practice_type_code = row[0]
                    code.name = row[1]
                    code.description = row[2]
                    if row[3] not in ['Blank']:
                        code.discovery_rate = row[3]
                    code.save()

                print ('Imported: {} codes'.format(ProcessCode.objects.count()))

