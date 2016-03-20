from django.core.management.base import BaseCommand
from django_engvtweb.team_order.utils import import_new_qbpcatalog, DEFAULT_PARTS_FILE


class Command(BaseCommand):

    def handle(self, *args, **options):
        filepath = DEFAULT_PARTS_FILE
        self.stdout.write('== Beginning import of QBP Catalog using file: %s ==' % filepath)
        import_new_qbpcatalog(filepath)
        self.stdout.write('== Done ==')
