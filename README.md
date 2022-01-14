# Xumm Python library

## Installation

```bash
pip3 install git+https://github.com/CASL-AE/xumm-py
```

To install from source, run

```bash
git clone https://github.com/CASL-AE/xumm-py
cd xumm
python setup.py install
```

## Documentation

Please see the [Xumm API Documentation](https://xumm.readme.io/docs/introduction) for the most up-to-date API documentation.

### Usage

This library has only been tested using Python 3.9.?.

Getting and interacting with accounts:

```python
import xumm

xumm.env = 'production'
xumm.api_key = 'xxx'
xumm.api_secret = 'xxx'
xumm.api_version = 'v1'

payload_id = 'xxxx-xxxx-xxxx-xxxx'
payload_data = xumm.Payload.get(payload_id)

custom_meta = payload_data.custom_meta
print(custom_meta)
```

### Submitting a payload

```python
payload = {
  'txjson': {
    'TransactionType': 'Signin'
  },
  'options': {
    'expire': 240,
    'submit': False,
    'return_url': {
      'web': 'https://example.com/signin'
    },
  }
}
response = xumm.Payload.post(payload)
print(response.payload_id)
```

## Development


### Install Virtual ENV - (Skip)

We use virtualenv. Install with `[sudo] pip3 install virtualenv`, initialize with `virtualenv venv`, and activate with `source venv/bin/activate`.

### Create VirtualEnv and Install requirements

Already have Virtualenv installed:

```bash
mkvirtualenv xumm-py \
&& pip3 install -r requirements.txt
```

### Testing

To run the test suite, run `py.test` from the project root.

### Linting

We enforce linting on the code with flake8. Run with `flake8 xumm` from the project root.

```bash
flake8 xumm --output-file logs/linter.txt
```


### TODO

scripts/

for bumping major/minor/patch