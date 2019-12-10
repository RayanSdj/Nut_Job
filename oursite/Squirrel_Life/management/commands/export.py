from django.core.management.base import BaseCommand, CommandError
from Squirrel_Life.models import Squirrel
import csv

class Command(BaseCommand):
    help='export the csv file into our database'

    def add_arguments(self, parser):
        parser.add_argument('new_file', type=str)

    
    def handle(self, *args, **options):
        path_csv_file=options['csv_file']
        with open(path_csv_file) as f:
            reader=csv.reader(f, delimeter='\n')
            i=0
            for row in reader:
                if row in reader:
                    if i>1:
                        new_Squirrel = Squirrel.objects.create(X=row[0], Y=row[1], Unique_Squirrel_ID=row[2], Hectare=row[3], Shift=row[4], date=row[5], Hectare_Squirrel_Number=row[6], Age=row[7], Primary_Fur_Color=row[8], Highlight_Fur_Color=row[9], Combination_of_Primary_and_Highlight_Color=row[10])

                        new_squirrel.save()

                    i+=1
