from fetch_products import FetchProducts
from products_analysis import ProductsAnalysis
from record_keys import RecordKeys


class ProductsReport:
    if __name__ == '__main__':
        FetchProducts.fetch_products()
        records = FetchProducts.records
        new_prices = [int(record[RecordKeys.NEW_PRICE]) for record in records]
        brands_price = {record[RecordKeys.BRAND]: int(record[RecordKeys.NEW_PRICE]) for record in records}
        print('Product Max Price:', max(new_prices))
        print('Product Min Price:', min(new_prices))
        print('Brand Wise Max Price:',
              ProductsAnalysis.brand_wise_max_prices(brands_price))
        print('Brand Wise Min Price:',
              ProductsAnalysis.brand_wise_min_prices(brands_price))
        print('Max Discounted Product Ratio:', max(ProductsAnalysis.max_discounted_ratio().values()))
        print('Brand Wise Max Discounted Product Ratio:', ProductsAnalysis.max_discounted_ratio())
