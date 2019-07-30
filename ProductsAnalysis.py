from fractions import Fraction
from ReadProductsFromCSV import *


class ProductsAnalysis:

    # method calculate the product max discounted ratio
    @staticmethod
    def max_discounted_ratio_item():
        discounted_products_ratio = []

        for record in ReadProductsFromCSV.get_records(Constant.DISCOUNT_RATIO):
            discount_ratio = Fraction(record[2], record[3])
            if discount_ratio > 1:
                discounted_products_ratio.append((record[1], str(discount_ratio)))

        return discounted_products_ratio

    # method brand wise max/min price calculation
    @staticmethod
    def brand_wise_max_min_prices(find_what, brands_price_dict):
        for record in ReadProductsFromCSV.get_records(Constant.BRAND_RECORDS):
            brand_name = record[0]
            price = record[1]
            for brand_key, previous_price in brands_price_dict.items():
                if brand_name == brand_key:
                    if find_what == Constant.FIND_MAX and previous_price < price:
                        brands_price_dict[brand_key] = price
                    elif find_what == Constant.FIND_MIN and previous_price > price:
                        brands_price_dict[brand_key] = price

        return brands_price_dict
