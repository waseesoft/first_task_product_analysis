from fractions import Fraction
from fetch_products import FetchProducts
from constant import Constant


class ProductsAnalysis:

    @staticmethod
    def max_discounted_products_ratio_dict():
        discounted_products_ratio = []

        for record in FetchProducts.records:
            discount_ratio = Fraction(int(record[Constant.OLD_PRICE]), int(record[Constant.NEW_PRICE]))
            if discount_ratio > 1:
                discounted_products_ratio.append((record[Constant.BRAND], str(discount_ratio)))

        return dict(discounted_products_ratio)

    @staticmethod
    def brand_wise_max_min_prices(find_what, brands_price_dict):
        for record in FetchProducts.records:
            brand = record[Constant.BRAND]
            price = int(record[Constant.NEW_PRICE])

            for brand_key, previous_price in brands_price_dict.items():
                if brand == brand_key:
                    if find_what == Constant.FIND_MAX and int(previous_price) < price:
                        brands_price_dict[brand_key] = price
                    elif find_what == Constant.FIND_MIN and int(previous_price) > price:
                        brands_price_dict[brand_key] = price

        return brands_price_dict
