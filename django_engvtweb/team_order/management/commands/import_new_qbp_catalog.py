from django.core.management.base import BaseCommand
from django_engvtweb.team_order.utils import import_new_qbpcatalog, DEFAULT_PARTS_FILE


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--filepath',
                            action='store_true',
                            dest='filepath',
                            default=False,
                            help='Full path to qbpcatalog.txt file')

    def handle(self, *args, **options):
        if options['filepath']:
            filepath = options['filepath']
        else:
            filepath = DEFAULT_PARTS_FILE
        self.stdout.write('== Beginning import of QBP Catalog using file: %s ==' % filepath)
        import_new_qbpcatalog(filepath)
        self.stdout.write('== Done ==')
