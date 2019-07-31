import csv


class FetchProducts:
    records = []

    @staticmethod
    def fetch_products():
        file_name = 'raw_files\\marc.csv'
        with open(file_name, 'r', encoding='utf8') as file:
            dict_reader = csv.DictReader(file)
            for record in dict_reader:
                FetchProducts.records.append(record)
