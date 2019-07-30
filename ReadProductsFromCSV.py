import csv
from Constant import *


class ReadProductsFromCSV:

    @staticmethod
    def get_records(records_tag):
        file_name = 'raw_files\\marc.csv'
        records = []
        with open(file_name, 'r', encoding='utf8') as csv_file:
            # Read the Titles
            csv_file.readline()

            for col in csv.reader(csv_file):
                new_price = int(col[5])
                old_price = int(col[4])
                brand_name = col[3]

                if records_tag == Constant.NEW_PRICES:
                    records.append(new_price)
                elif records_tag == Constant.OLD_PRICES:
                    records.append(old_price)
                elif records_tag == Constant.BRAND_RECORDS:
                    records.append((brand_name, new_price))
                elif records_tag == Constant.DISCOUNT_RATIO:
                    records.append((col[2], brand_name, old_price, new_price))
        return records

