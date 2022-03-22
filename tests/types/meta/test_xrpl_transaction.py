#!/usr/bin/env python
# coding: utf-8

import pytest
from testing_config import BaseTestConfig

from xumm.resource.types import (
    XrplTransaction
)

class TestXrplTransactionResponse(BaseTestConfig):

    def test_xrpl_tx_response(cls):
        print('should set xrpl tx response')

        dict = cls.json_fixtures['xrplTx']
        cls.assertEqual(XrplTransaction(**dict).to_dict(), dict)

    def test_xrpl_tx_response_fail(cls):
        print('should fail to xrpl tx details')

        dict = {
            "txid": 1,  # FAILS
            "balanceChanges": {
                "r4bA4uZgXadPMzURqGLCvCmD48FmXJWHCG": [
                        {
                            "counterparty": "",
                            "currency": "XRP",
                            "value": "-1.000012"
                        }
                ],
                "rPdvC6ccq8hCdPKSPJkPmyZ4Mi1oG2FFkT": [
                    {
                        "counterparty": "",
                        "currency": "XRP",
                        "value": "1"
                    }
                ]
            },
            "node": "wss://xrplcluster.com",
            "transaction": {
                "Account": "r4bA4uZgXadPMzURqGLCvCmD48FmXJWHCG",
                "Amount": "1000000",
                "Destination": "rPdvC6ccq8hCdPKSPJkPmyZ4Mi1oG2FFkT",
                "Fee": "12",
                "Flags": 2147483648,
                "Sequence": 58549314,
                "SigningPubKey": "0260F06C0590C470E7E7FA9DE3D9E85B1825E19196D8893DD84431F6E9491739AC",
                "TransactionType": "Payment",
                "meta": {
                    "TransactionIndex": 0,
                    "TransactionResult": "tesSUCCESS",
                    "delivered_amount": "1000000"
                },
                "validated": True
            }
        }

        with pytest.raises(ValueError, match=r"Invalid value: 1 for `txid`, must be a `<class 'str'>` found: <class 'int'>"):
            XrplTransaction(**dict)
            cls.fail("XrplTransaction: raised Exception unexpectedly!")