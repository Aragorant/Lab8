from django.core.management.base import BaseCommand
from myapp1.models import Subjects

class Command(BaseCommand):
    help = 'Populate Subjects table with data'

    def handle(self, *args, **options):
        subjects_data = [
            (1, 'Математика', 60, 2),
            (2, 'Історія', 45, 3),
            (3, 'Фізика', 30, 2)
        ]

        for data in subjects_data:
            subject = Subjects(
                Subject_id=data[0],
                Title=data[1],
                Hours_per_semester=data[2],
                Number_of_semesters=data[3]
            )
            subject.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated Subjects table'))
