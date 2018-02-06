#!/usr/bin/env bash

. activate

echo "Removing local copies of old catalog"
rm ~/qbpcatalog*

echo "Now downloading new catalog..."
curl "https://qbp.com/diagrams/newsite/product_data/qbpcatalog.txt" > ~/qbpcatalog-ascii.txt

echo "Removing non-ASCII characters..."
iconv -f ASCII -t utf-8//IGNORE qbpcatalog-ascii.txt > ~/qbpcatalog.txt

echo "Beginning catalog import. All old catalog objects will be purged!!"
python manage.py import_new_qbp_catalog

echo "Rebuilding search index..."
python manage.py rebuild_index

echo "Done!"
exit 0