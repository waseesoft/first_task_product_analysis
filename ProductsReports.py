from ProductsAnalysis import *


class ProductsReport:

    @staticmethod
    def show_products_analysis_reports():
        # max_price_product
        print('Product Max Price:', max(ReadProductsFromCSV.get_records(Constant.NEW_PRICES)))
        # min_price_product
        print('Product Min Price:', min(ReadProductsFromCSV.get_records(Constant.NEW_PRICES)))

        # get the brands record form csv file
        brands_record = ReadProductsFromCSV.get_records(Constant.BRAND_RECORDS)

        # brand_wise_max_price_product
        brands_max_price_dict = dict(brands_record)
        print('\nBrand Wise Max Price:',
              ProductsAnalysis.brand_wise_max_min_prices(Constant.FIND_MAX, brands_max_price_dict))

        # brand_wise_min_price_product
        brands_min_price_dict = dict(brands_record)
        print('Brand Wise Min Price:',
              ProductsAnalysis.brand_wise_max_min_prices(Constant.FIND_MIN, brands_min_price_dict))

        # max_discounted_ratio_item
        print('\nMax Discounted Product Ratio:', max(dict(ProductsAnalysis.max_discounted_ratio_item()).values()))

        # brand_wise_max_discounted_ratio_item
        print('Brand Wise Max Discounted Product Ratio:', dict(ProductsAnalysis.max_discounted_ratio_item()))

