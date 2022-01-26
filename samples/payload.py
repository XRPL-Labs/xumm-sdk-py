#!/usr/bin/env python
# coding: utf-8

import binascii

payload = {
  'custom_meta': {
    'instruction': 'Hey! Please sign for:\n\nThis\nand\nthat 🍻',
    'blob': {
      'myOwnProp': 'Whereever',
      'clientCountry': 'Estonia',
      'clientAge': 34
    },
    'identifier': 'MY_OWN_UNIQUE_INTERNAL_ID_123'
  },
  'options': {
    'submit': True,
    'multisign': False,
    'expire': 500,
    'return_url': {
      'app': 'https://dangell.com/xrpl?payload={}'.format(id),
      'web': 'https://dangell.com/xrpl?payload={}'.format(id)
    }
  },
  'user_token': '7ccc19cf-970a-4185-8bd3-49d507bf24ae',
  # 'txblob': '1200002400000003614000000002FAF0806840000000000000C8732' +
  #   '...' +
  #   '5727D0B4057696574736557696E64E1F1',
  'txjson': {
    'TransactionType' : 'Payment',
    'Destination' : 'rdAngelle2wMz3SBnAG8hkMsCgvGy9LWbZ1',
    'Amount': '1000000',
    'LastLedgerSequence': 20,
    'Fee': '1337',
    'Memos': [
      {
        'Memo': {
          'MemoData': binascii.hexlify('Sample XUMM payload'.encode('utf8')).decode('utf-8').upper(),
          'MemoFormat': binascii.hexlify('some/memo'.encode('utf8')).decode('utf-8').upper(),
        }
      }
    ]
  }
})