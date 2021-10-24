import pandas as pd
import re

from django.core.management import BaseCommand

from api.models import Phone


class Command(BaseCommand):
    help = 'Import phone numbers to DB'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Path to excel file')
        parser.add_argument('column', type=str, help='Name of column in excel table')
        parser.add_argument('-f', '--full', action='store_true', help='Drop DB before import')

    def handle(self, *args, **kwargs):
        if kwargs['full']:
            Phone.objects.all().delete()

        excel = pd.read_excel(io=kwargs['path'], engine='openpyxl')

        for _, row in excel.iterrows():
            frm_number = re.sub('[^0-9a-zA-Z]+', '', str(row[kwargs['column']]).replace('+7', '8'))

            if not Phone.objects.filter(number=frm_number).exists():
                Phone(number=frm_number).save()
                print(f'Added number {frm_number}')
            else:
                print(f'Number {frm_number} is already in db')
