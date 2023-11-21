import json
from datetime import datetime

from django.utils.text import slugify
from django.core.management.base import BaseCommand, CommandError
from hr_system.entities.models import Employee, Industry, GENDER_CHOICES


NOT_SET = 'n/a'


class Command(BaseCommand):
    help = "Import data from json file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        path = options['file_path']

        with open(path, 'r') as f:
            data = json.loads(f.read())
            for entry in data:
                self.process(entry)

    @staticmethod
    def process_industry(industry_name: str) -> Industry:
        industry_slug = slugify(industry_name)
        industry = Industry.objects.filter(slug=industry_slug).first()
        if not industry:
            industry = Industry.objects.create(
                name=industry_name,
                slug=industry_slug,
            )
            print(f"Saved industry {industry}")
        return industry


    def process(self, entry):
        if Employee.objects.filter(id=entry['id']).exists():
            print(f"Employee with id {entry['id']} already exists, skipping.")
            return

        if entry['industry']:
            industry = self.process_industry(entry['industry'])
        else:
            industry = None
        
        if entry['date_of_birth']:
            dob = datetime.strptime(entry['date_of_birth'], '%d/%m/%Y')
        else:
            dob = None

        employee = Employee.objects.create(
            id=entry['id'],
            first_name=entry['first_name'],
            last_name=entry['last_name'],
            email=entry['email'],
            gender=entry['gender'],
            date_of_birth=dob,
            industry=industry,
            salary=entry['salary'],
            years_experience=entry['years_of_experience'],
        )
        print(f'created {employee}')
        
