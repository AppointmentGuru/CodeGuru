import xmltodict
from django.core.management.base import BaseCommand
from api.models import ICD10Code

def __get_title_text(term):
    title = term.get('title')
    if str(title) != title:
        title = title.get('text')
    return title

def create_term(term, parent):
    if term is None: return False

    try:
        code = term.get('code')
        see = term.get('see')
        title = __get_title_text(term)

        obj = ICD10Code.objects.create(
                code=code,
                title=title,
                see = see,
                parent=parent
              )
        sub_terms = term.get('term', None)
        # print ('created: {}: {}'.format(code, title))
        if sub_terms is not None:
            for new_term in sub_terms:
                print('--> creating sub term')
                create_term(new_term, obj)
        else:
            return False
    except AttributeError:
        print(term)
        pass


class Command(BaseCommand):
    help = 'Import ICD10 codes'

    def handle(self, *args, **options):

        for t in ICD10Code.objects.all(): t.delete()

        f = open('data/ICD10CM_FY2017_Full_XML/icd10cm_index_2017.xml')
        xmlstring = f.read()
        doc = xmltodict.parse(xmlstring)

        for letter in doc['ICD10CM.index']['letter']:
            print(letter.get('title'))
            for main_term in letter.get('mainTerm'):

                # code = main_term.get('code')
                # title = main_term.get('title')
                # obj = ICD10Code.objects.create(code=code, title=title)

                # print ('Mainterm: {}: {}'.format(main_term.get('code'), main_term.get('title')))
                create_term(main_term, None)