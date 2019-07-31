from products_analysis import ProductsAnalysis
from fetch_products import FetchProducts
from constant import Constant


class ProductsReport:

    if __name__ == '__main__':

        FetchProducts.fetch_products()
        records = FetchProducts.records
        new_prices = [int(record[Constant.NEW_PRICE]) for record in records]
        brands_price_dict = dict([(record[Constant.BRAND], int(record[Constant.NEW_PRICE])) for record in records])

        print('Product Max Price:', max(new_prices))
        print('Product Min Price:', min(new_prices))

        print('Brand Wise Max Price:',
              ProductsAnalysis.brand_wise_max_min_prices(Constant.FIND_MAX, brands_price_dict))
        print('Brand Wise Min Price:',
              ProductsAnalysis.brand_wise_max_min_prices(Constant.FIND_MIN, brands_price_dict))

        print('Max Discounted Product Ratio:', max(ProductsAnalysis.max_discounted_products_ratio_dict().values()))
        print('Brand Wise Max Discounted Product Ratio:', ProductsAnalysis.max_discounted_products_ratio_dict())
