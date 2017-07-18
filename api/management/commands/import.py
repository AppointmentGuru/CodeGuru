import xmltodict
from django.core.management.base import BaseCommand
from api.models import ICD10Code, Code
from collections import OrderedDict

def is_list(node):
    return getattr(node, 'append', None) is not None

def normalize_node(node):
    '''Normalize all notes to be lists'''
    if is_list(node):
        return node
    else:
        return [node]

def save_code(code, count):
    print ('--------------')
    outdent = ('___').join(['' for x in range(0, count)])
    print('    |___{} {}: {}'.format(outdent, code.get('name'), code.get('desc')))

    fields = ['includes', 'excludes1', 'excludes2', 'inclusionTerm', 'useAdditionalCode']
    fields_map = {
        'includes': 'includes',
        'excludes1': 'excludes1',
        'excludes2': 'excludes2',
        'inclusionTerm': 'inclusion_term',
        'useAdditionalCode': 'use_additional_code',
    }
    data = {
        "name": code.get('name'),
        "description": code.get("desc")
    }
    for field in fields:
        field_notes = code.get(field, None)
        notes_array = []
        if field_notes is not None:
            field_notes = normalize_node(field_notes)
            print('{}** {}'.format(outdent, field))
            for field_note in field_notes:
                notes = normalize_node(field_note.get('note', []))
                for note in notes:
                    notes_array.append(note)
                    print('{}  * {}'.format(outdent, note))

        data[fields_map.get(field)] = notes_array

    Code.objects.create(**data)

def recurse_codes(code, count=1, parent=None):

    save_code(code, count)
    sub_codes = normalize_node(code.get('diag', []))
    if len(sub_codes) == 0:
        return code

    for sub_code in sub_codes:
        recurse_codes(sub_code, count + 1, parent=code)

class Command(BaseCommand):
    help = 'Import ICD10 codes'

    def handle(self, *args, **options):

        for t in Code.objects.all(): t.delete()

        # f = open('data/ICD10CM_FY2017_Full_XML/test.xml')
        f = open('data/ICD10CM_FY2017_Full_XML/icd10cm_tabular_2017.xml')
        xmlstring = f.read()
        doc = xmltodict.parse(xmlstring)

        for chapter in doc['ICD10CM.tabular']['chapter']:
            print('- {}'.format(chapter.get('name')))
            for section in chapter['section']:
                print(' |__ {}'.format(section.get('desc')))

                section_codes = normalize_node(section.get('diag', []))
                for code in section_codes:
                    recurse_codes(code, count=1)







