from django.core.management.base import BaseCommand, CommandError
from django_engvtweb.team_order.models import *
from django_engvtweb.team_order.utils import import_new_qbpcatalog
from optparse import make_option

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--brand',
            action='store',
            dest='brand',
            default=False,
            help='Name of parts brand'),
        make_option('--category',
            action='store',
            dest='category',
            default=False,
            help='Name of parts category'),
        )

    args = "<bike/part> <path_to_csv_file>"

    part_types = {'bike': Bike,
                  'part': OtherPart}

    def handle(self, *args, **options):
        model = self.part_types[args[0]]
        try:
            filepath = args[1]
            self.stdout.write('== CSV File %s found ==' % filepath)
        except IndexError:
            raise Exception('Must specify a file path to your CSV as second argument')

        #get models
        brand_model = model.brand.field.related.parent_model
        category_model = model.category.field.related.parent_model

        #parse optional brand and category arguments
        brand = None
        if options['brand']:
            brand, created = brand_model.objects.get_or_create(name=options['brand'])
            if created:
                self.stdout.write('== Created new brand: %s ==' % brand)
            else:
                self.stdout.write('== Found brand object: %s ==' % brand)

        category = None
        if options['category']:
            category, created = category_model.objects.get_or_create(name=options['category'])
            if created:
                self.stdout.write('== Created new category: %s ==' % brand)
            else:
                self.stdout.write('== Found category object: %s ==' % brand)

        self.stdout.write('== Now creating objects from CSV... ==')

        parts = model.bulk_create_from_csv(filepath, brand=brand, category=category)

        self.stdout.write('== Success! ==')
        self.stdout.write('== Created the following %s %s objects: ==' % (len(parts), model.__name__))
        self.stdout.write('\n'.join([unicode(p) for p in parts]))