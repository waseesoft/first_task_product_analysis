import csv
from fractions import Fraction

file_name = 'marc.csv'
new_prices = []
old_prices = []
brands_record = []
discounted_products = []

with open(file_name, 'r', encoding='utf8') as csv_file:
    csv_file.readline()

    for col in csv.reader(csv_file):
        new_price = int(col[5])
        old_price = int(col[4])

        new_prices.append(new_price)
        old_prices.append(old_price)
        brands_record.append((col[3], new_price))

        # calculate product discount ratio
        discount_ratio = Fraction(old_price, new_price)
        if discount_ratio > 1:
            discounted_products.append((col[1], str(discount_ratio)))


brands_max_price_dict = dict(brands_record)
brands_min_price_dict = dict(brands_record)
find_min, find_max = 'min', 'max'


def brand_wise_max_min_prices(find_what, brands_price_dict):
    for record in brands_record:
        brand_name = record[0]
        price = record[1]
        for brand_key, previous_price in brands_price_dict.items():
            if brand_name == brand_key:
                if find_what == find_max and previous_price < price:
                    brands_price_dict[brand_key] = price
                elif find_what == find_min and previous_price > price:
                    brands_price_dict[brand_key] = price

    return brands_price_dict


# max_price_product
print('Product Max Price:', max(new_prices))
# min_price_product
print('Product Min Price:', min(new_prices))

# brand_wise_max_price_product
print("\nBrand Wise Max Price:", brand_wise_max_min_prices(find_max, brands_max_price_dict))
# brand_wise_min_price_product
print('Brand Wise Min Price:', brand_wise_max_min_prices(find_min, brands_min_price_dict))

# max_discounted_ratio_item
print('\nMax Discounted Products Id & ratio:', dict(discounted_products))
