import pandas
import os
from django.db.transaction import atomic
from models import *

DEFAULT_PARTS_FILE = os.path.expanduser('~/qbpcatalog.txt')


@atomic
def import_new_qbpcatalog(file):

    # read data into dataframe to make things quick
    df = pandas.io.parsers.read_csv(file, sep='\t', header=0)
    df = df.fillna('None')

    # clear all old data
    QbpPart.objects.all().delete()
    QbpBrand.objects.all().delete()

    # now create brands
    unique_brands = df['Brand'].unique()
    brand_objs = [QbpBrand(name=removeNonAscii(k)) for k in unique_brands]
    QbpBrand.objects.bulk_create(brand_objs)

    # get ids in dict to speed up bulk create of objects
    # this will avoid a new query for each row
    brand_values = QbpBrand.objects.all().values()
    # make it easier to work with here
    brand_values = dict([(i['name'], i['id']) for i in brand_values])

    n = lambda v: None if v == 'None' else v
    b = lambda v: True if v == 'Yes' else False

    # create
    parts_objs = []
    for i in range(0, len(df)):
        row = df.ix[i]
        part = QbpPart(prodid=row.ProdID,
                       UPC=n(row.UPC),
                       category=row.Category,
                       brand_id=brand_values[removeNonAscii(row.Brand)],
                       model=row.Model,
                       model_description=n(removeNonAscii(row['Model Description'])),
                       size=n(removeNonAscii(row.Size)),
                       color=n(row.Color),
                       msrp=row.MSRP,
                       map=row.MAP,
                       unit_price=row['Each Cost'],
                       manufacturer_prod=n(row['Manufacturer Prod']),
                       coo=n(row.COO),
                       discontinued=b(row.Discontinued),
                       uom=n(row.UOM),
                       weight=row.Weight,
                       length=row.Length,
                       width=row.Width,
                       height=row.Height,
                       ormd=b(row.ORMD),
                       description=removeNonAscii(row['Product Description']),
                       replacement=n(row.Replacement),
                       substitute=n(row.Substitute))
        parts_objs.append(part)
    # finally, bulk create all parts
    QbpPart.objects.bulk_create(parts_objs)
