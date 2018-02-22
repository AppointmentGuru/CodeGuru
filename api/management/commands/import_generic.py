from django.core.management.base import BaseCommand
from api.models import ProcessCode
import csv

class Command(BaseCommand):
    help = 'Import ICD10 codes'

    def handle(self, *args, **options):

        # this is the only part you should need to configure
        file = '/code/codes.csv'
        mapping = {
            "practice_type_code": [1],
            "name": [1,0],
            "description": [2]
        }

        with open(file) as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            count = 0
            for row in reader:
                data = {}
                for key, cols in mapping.items():
                    str = ('').join([row[col_index] for col_index in cols])
                    data[key] = str
                print(data)
                ProcessCode.objects.create(**data)
                count = count + 1
            print("- {}: {} records".format(file, count))

        print ('Imported: {} codes'.format(ProcessCode.objects.count()))

