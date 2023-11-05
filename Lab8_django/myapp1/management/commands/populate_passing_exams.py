from django.core.management.base import BaseCommand
from myapp1.models import Passing_exams
from datetime import date

class Command(BaseCommand):
    help = 'Populate Passing_exams table with data'

    def handle(self, *args, **options):
        passing_exams_data = [
            ('2023-01-15', 1, 1, 5),
            ('2023-02-20', 2, 2, 4),
            ('2023-03-25', 3, 3, 3),
            ('2023-04-10', 4, 1, 5),
            ('2023-05-18', 5, 2, 4),
            ('2023-06-30', 6, 3, 3),
            ('2023-01-15', 7, 1, 5),
            ('2023-02-20', 8, 2, 4),
            ('2023-03-25', 9, 3, 3),
            ('2023-04-10', 10, 1, 5),
            ('2023-05-18', 1, 2, 4),
            ('2023-06-30', 2, 3, 3),
            ('2023-01-15', 3, 1, 5),
            ('2023-02-20', 4, 2, 4),
            ('2023-03-25', 5, 3, 3),
            ('2023-04-10', 6, 1, 5),
            ('2023-05-18', 7, 2, 4),
            ('2023-06-30', 8, 3, 3),
            ('2023-01-15', 9, 1, 5),
            ('2023-02-20', 10, 2, 4)
        ]

        for data in passing_exams_data:
            passing_exam = Passing_exams(
                Date_of_passing=date.fromisoformat(data[0]),
                Student_id_id=data[1],
                Subject_id_id=data[2],
                Score=data[3]
            )
            passing_exam.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated Passing_exams table'))
