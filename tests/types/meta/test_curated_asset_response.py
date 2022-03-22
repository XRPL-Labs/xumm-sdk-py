#!/usr/bin/env python
# coding: utf-8

from testing_config import BaseTestConfig

from xumm.resource.types import (
    CuratedAssetsResponse
)

class TestCuratedAssetResponse(BaseTestConfig):

    def test_curated_asset_response(cls):
        print('should set curated asset response')

        dict = cls.json_fixtures['curatedAssets']
        cls.assertEqual(CuratedAssetsResponse(**dict).to_dict(), dict)

    def test_curated_asset_response_fail(cls):
        print('should fail to set application details')

        dict = {
            "issuers": [
                "Bitstamp",
                "Wietse"
            ],
            "currencies": [
                "USD",
                "BTC",
                "ETH",
                "WIE"
            ],
            "details": {
                "Bitstamp": {
                    "id": 185,
                    "name": 1,  # FAILS
                    "domain": "bitstamp.net",
                    "avatar": "https://xumm.app/assets/icons/currencies/ex-bitstamp.png",
                    "shortlist": 1,
                    "currencies": {
                        "USD": {
                            "id": 178,
                            "issuer_id": 185,
                            "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
                            "currency": "USD",
                            "name": "US Dollar",
                            "avatar": "https://xumm.app/assets/icons/currencies/fiat-dollar.png",
                            "shortlist": 1
                        },
                        "BTC": {
                            "id": 492,
                            "issuer_id": 185,
                            "issuer": "rvYAfWj5gh67oV6fW32ZzP3Aw4Eubs59B",
                            "currency": "BTC",
                            "name": "Bitcoin",
                            "avatar": "https://xumm.app/assets/icons/currencies/crypto-btc.png",
                            "shortlist": 1
                        }
                    }
                },
                "Wietse": {
                    "id": 17553,
                    "name": "Wietse",
                    "domain": "wietse.com",
                    "avatar": "https://xumm.app/assets/icons/currencies/wietse.jpg",
                    "shortlist": 0,
                    "currencies": {
                        "WIE": {
                            "id": 17552,
                            "issuer_id": 17553,
                            "issuer": "rwietsevLFg8XSmG3bEZzFein1g8RBqWDZ",
                            "currency": "WIE",
                            "name": "Wietse",
                            "avatar": "https://xumm.app/assets/icons/currencies/transparent.png",
                            "shortlist": 0
                        }
                    }
                }
            }
        }

        with pytest.raises(ValueError, match=r"Invalid value: 1 for `name`, must be a `<class 'str'>` found: <class 'int'>"):
            CuratedAssetsResponse(**dict)
            cls.fail("CuratedAssetsResponse: raised Exception unexpectedly!")