#!/usr/bin/env python
# coding: utf-8

import binascii
from uuid import uuid4

payload = {
  'custom_meta': {
    'instruction': 'Hey! Please sign for:\n\nThis\nand\nthat 🍻',
    'blob': {
      'myOwnProp': 'Whereever',
      'clientCountry': 'Moon',
    },
    'identifier': str(uuid4())
  },
  'options': {
    'submit': True,
    'multisign': False,
    'expire': 500,
    'return_url': {
      'app': 'https://example.com/callback?payload={id}&blob={txblob}',
      'web': 'https://example.com/callback?identifier={cid}&tx={txid}'
    }
  },
  'txjson': {
    'TransactionType' : 'Payment',
    'Destination' : 'rPEPPER7kfTD9w2To4CQk6UCfuHM9c6GDY',
    'DestinationTag': 495,
    'Amount': '1337',
    'LastLedgerSequence': 20,
    'Fee': '12',
    'Memos': [
      {
        'Memo': {
          'MemoData': binascii.hexlify('Sample XUMM payload'.encode('utf8')).decode('utf-8').upper(),
          'MemoFormat': binascii.hexlify('some/memo'.encode('utf8')).decode('utf-8').upper(),
        }
      }
    ]
  }
}