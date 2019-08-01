from fractions import Fraction

from fetch_products import FetchProducts
from record_keys import RecordKeys


class ProductsAnalysis:
    @staticmethod
    def max_discounted_products_ratio_dict():
        discounted_ratios = {}
        for record in FetchProducts.records:
            discount_ratio = Fraction(int(record[RecordKeys.OLD_PRICE]), int(record[RecordKeys.NEW_PRICE]))
            if discount_ratio > 1:
                discounted_ratios[record[RecordKeys.BRAND]] = str(discount_ratio)

        return discounted_ratios

    @staticmethod
    def brand_wise_max_prices(brands_price):
        for record in FetchProducts.records:
            price = int(record[RecordKeys.NEW_PRICE])
            for brand, previous_price in brands_price.items():
                if brand == record[RecordKeys.BRAND] and price > previous_price:
                    brands_price[brand] = price

        return brands_price

    @staticmethod
    def brand_wise_min_prices(brands_price):
        for record in FetchProducts.records:
            price = int(record[RecordKeys.NEW_PRICE])
            for brand, previous_price in brands_price.items():
                if brand == record[RecordKeys.BRAND] and price < previous_price:
                    brands_price[brand] = price

        return brands_price
