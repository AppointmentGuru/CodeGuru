from django.core.management.base import BaseCommand
from api.models import Code
import json

class Command(BaseCommand):
    help = 'Supplement existing icd10 codes from a json file'

    def handle(self, *args, **options):
        with open('api/spiders/codes.json') as f:
            data = json.loads(f.read())
            count = 0
            for code in data:
                name = code.get('code')
                if not Code.objects.filter(name=name).exists():
                    data = {
                        'name': name,
                        'description': code.get('description')
                    }
                    Code.objects.create(**data)
                    print(name)
                    count = count+1

        print('Imported {} records'.format(count))