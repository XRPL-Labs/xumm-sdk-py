# Xumm Python library

[![CircleCI](https://circleci.com/bb/Harpangell/xumm-python/tree/master.svg?style=svg&circle-token=3e47a0118e8b37d59b9dae0d884468d3f8f94c99)](https://circleci.com/bb/Harpangell/xumm-python/tree/master)

## Installation

```bash
pip install git+git://bitbucket.org/Harpangell/xumm-python.git@master
```

To install from source, run

```bash
git clone https://Harpangell@bitbucket.org/Harpangell/xumm-python.git
cd xumm
python setup.py install
```

## Documentation

Please see the [Xumm API Documentation](https://api-co.xumm.com/Documentation/#getting-started) for the most up-to-date API documentation.

### Usage

This library has only been tested using Python 3.6.?.

Getting and interacting with accounts:

```python
import xumm

xumm.env = 'production'
xumm.api_key = 'xxx'
xumm.api_secret = 'xxx'
xumm.api_version = 'v1'

client = xumm.Account()

properties = client.properties
propertyName = properties[0].name
print(propertyName)
```

Properties are cached on each model instance. To refresh, do `property = client.get_property(propertyID)`. (TODO: allow properties to be refreshed manually)

Objects embedded in API responses are added as properties on each model instance. To refresh, do `properties.refresh()`.

Interacting with sales:

```python

new_transactions = [
  {
    packageLabel = 'ABCDEF012345670000010331',
    quantity = 1.0,
    unitOfMeasure = 'Ounces',
    totalAmount = 9.99,
  },
  {
    packageLabel = 'ABCDEF012345670000010332',
    quantity = 1.0,
    unitOfMeasure = ,
    totalAmount = 9.99,
  }
]

sales_date_time = datatime.utcnow()
sales_customer_type = 'Consumer'
patient_license_number = None
caregiver_license_number = None
identification_method = None
transactions = new_transactions

sales_receipt = facility.create_sales_receipt(
    sales_date_time,
    sales_customer_type,
    patient_license_number,
    identification_method,
    transactions,
)
print sales_receipt
# sales_receipt.void()
```

## Development

We use virtualenv. Install with `[sudo] pip install virtualenv`, initialize with `virtualenv venv`, and activate with `source venv/bin/activate`.

Install the development requirements with `pip install -r requirements/dev.txt`

### Testing

To run the test suite, run `py.test` from the project root.

### Linting

We enforce linting on the code with flake8. Run with `flake8 xumm` from the project root.

### TODOs

- create method for Listings
