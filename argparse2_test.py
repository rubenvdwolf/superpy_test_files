import argparse
import csv

# create parser
parser = argparse.ArgumentParser()
# create subparser
subparser = parser.add_subparsers(dest='command')

# subparser for buying a product
buy_product = subparser.add_parser('buy', help='add product to bought.csv')
buy_product.add_argument('--product', type=str,
                         metavar='', help='Product Name')
buy_product.add_argument('--price', type=float, metavar='',
                         help='price with at lease one decimal')
buy_product.add_argument('--expiration', type=str,
                         metavar='', help='add a date with notation YYYY-MM-DD')

sell_product = subparser.add_parser(
    'sell', help='move product from bought.csv to sold.csv')
sell_product.add_argument('--product', type=str,
                          metavar='', help='Product Name')
sell_product.add_argument('--price', type=float,
                          metavar='', help='price with at lease one decimal')

args = parser.parse_args()

if args.command == 'buy':
    total_product_info = [args.product, args.price, args.expiration]
    with open('bought.csv', 'a') as bought_product:
        new_line = csv.writer(bought_product)
        new_line.writerow(total_product_info)
if args.command == 'sell':
    pass
