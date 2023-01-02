from zipline.examples import buyapple
from zipline.api import order, record, symbol
import os

os.environ['ZIPLINE_ROOT'] = os.path.join(os.getcwd(), 'zipline')
print(os.environ['ZIPLINE_ROOT'])

def initialize(context):
    pass


def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price'))