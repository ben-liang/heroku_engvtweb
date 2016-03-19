from django.core.management.base import BaseCommand
from optparse import make_option
from django_engvtweb.team_order.utils import import_new_qbpcatalog, DEFAULT_PARTS_FILE

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--file',
            action='store',
            dest='file',
            default=False,
            help='Full path to qbpcatalog.txt file')
        )
    def handle(self, *args, **options):
        if options['file']:
            file = options['file']
        else:
            file = DEFAULT_PARTS_FILE
        self.stdout.write('== Beginning import of QBP Catalog using file: %s ==' % file)
        import_new_qbpcatalog(file)
        self.stdout.write('== Done ==')