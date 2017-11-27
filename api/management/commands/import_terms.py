'''
deprecated. Use import.py
'''
import xmltodict
from django.core.management.base import BaseCommand
from api.models import ICD10Code
from collections import OrderedDict

def __get_title_text(term):
    title = term.get('title')
    if str(title) != title:
        title = title.get('text')
    return title

def __is_leaf(term):
    return isinstance(term, OrderedDict)

def create_term(term, parent):
    if term is None: return False

    code = term.get('code')
    see = term.get('see')
    level = term.get('@level')
    title = __get_title_text(term)

    obj = ICD10Code.objects.create(
            code=code,
            title=title,
            see = see,
            parent=parent,
            level=level
          )
    print(obj.path)
    sub_terms = term.get('term', None)
    # print ('created: {}: {}'.format(code, title))
    if sub_terms is not None:
        if __is_leaf(sub_terms):
            create_term(sub_terms, obj)
        else:
            for new_term in sub_terms:
                create_term(new_term, obj)
    else:
        return False


class Command(BaseCommand):
    help = 'Import ICD10 codes'

    def handle(self, *args, **options):

        for t in ICD10Code.objects.all(): t.delete()

        # f = open('data/ICD10CM_FY2017_Full_XML/test.xml')
        f = open('data/ICD10CM_FY2017_Full_XML/icd10cm_index_2017.xml')
        xmlstring = f.read()
        doc = xmltodict.parse(xmlstring)
        for letter in doc['ICD10CM.index']['letter']:
            print(letter.get('title'))
            print('---------')

            is_leaf = isinstance(letter.get('mainTerm'), OrderedDict)
            if is_leaf:
                create_term(letter.get('mainTerm'), None)
            else:
                for main_term in letter.get('mainTerm', []):
                    create_term(main_term, None)




