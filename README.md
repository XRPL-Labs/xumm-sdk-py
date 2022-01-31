# XUMM SDK (PYTHON) [![python version](https://badge.fury.io/py/xumm-sdk-py.svg)](https://pypi.org/project/xumm-sdk-py/) [![GitHub Actions Python status](https://github.com/XRPL-Labs/xumm-sdk-py/workflows/Python/badge.svg?branch=main)](https://github.com/XRPL-Labs/xumm-sdk-py/actions)

Interact with the XUMM SDK from Python environments.

#### **Please note! The XUMM SDK (XUMM API in general) is for BACKEND USE only. Please DO NOT use your API credentials in a FRONTEND environment.**

> To implement the XUMM SKD (or XUMM API directly) in your own web project, make sure your frontend calls your own backend, where the follow up
communication with the XUMM SDK (or XUMM API) will take place. Your XUMM credentials should never be publicly available.

## How to use the XUMM SDK

Get the SDK straight from pypi: `pip3 install xumm-sdk-py`.

Initialize the SDK in Python (backend use):
```python
import xumm
```


Now continue by constructing the XummSdk object:

```python
sdk = xumm.XummSdk()
# Or with manually provided credentials (instead of using dotenv):
sdk = xumm.XummSdk('someAppKey', 'someAppSecret')
```

### Credentials

#### In case of backend use
The SDK will look in your environment or dotenv file (`.env`) for the `XUMM_APIKEY` and `XUMM_APISECRET` values. A `.env.sample` file is provided in this repository. A [sample dotenv file looks like this](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/.env.sample). Alternatively you can provide your XUMM API Key & Secret by passing them to the XummSdk constructor. 

If both your environment and the SDK constructor contain credentials, the values provided to the constructor will be used.

### Methods & params (+ samples)

After constructing the SDK, you can call the methods:

- `sdk.*` for the helper methods (see below)
- `sdk.payload.*` to get/update/create payloads for users to sign
- `sdk.storage.*` for your XUMM app storage (to store meta info for headless applications)

Please note all snippets below assume you constructed the XUMM SDK into the `sdk` constant, as the [How to use the XUMM SDK](#how-to-use-the-xumm-sdk) section outlines.

#### Helper methods

##### sdk.ping()

The `ping` method allows you to verify API access (valid credentials) and returns some info on your XUMM APP:

```python
pong = sdk.ping()
```

Returns [`<ApplicationDetails>`](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/xumm/resource/types/meta/application_details.py#L294):
```python
pong.quota  # {}
pong.application.name  # 'My XUMM APP'
pong.application.uuidv4  # '00000000-1111-2222-3333-aaaaaaaaaaaa'
pong.application.webhookurl  # ''
pong.application.disabled  # 0
pong.call.uuidv4  # 'bbbbbbbb-cccc-dddd-eeee-111111111111'
```

##### sdk.get_curated_assets()

The `get_curated_assets` method allows you to get the list of trusted issuers and IOU's. This is the same list used to
populate the "Add Asset" button at the XUMM home screan.

```python
curated_assets = sdk.get_curated_assets()
```

Returns [`<CuratedAssetsResponse>`](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/xumm/resource/types/meta/curated_assets_response.py#L426):
```python
curated_assets.issuers  # [ 'Bitstamp', 'GateHub' ]
curated_assets.currencies  # [ 'USD', 'BTC', 'EUR', 'ETH' ]
curated_assets.details.Bitstamp   # {}
curated_assets.details.GateHub   # {}
```


##### sdk.get_kyc_status()

The `get_kyc_status` return the KYC status of a user based on a user_token, issued after the
user signed a Sign Request (from your app) before (see Payloads - Intro).

If a user token specified is invalid, revoked, expired, etc. the method will always
return `NONE`, just like when a user didn't go through KYC. You cannot distinct a non-KYC'd user
from an invalid token.

Alternatively, KYC status can be retrieved for an XPRL account address: the address selected in
XUMM when the session KYC was initiated by.

```python
kyc_status = sdk.get_kyc_status('00000000-0000-0000-0000-000000000000')
```

... or using an account address:
```python
kyc_status = sdk.get_kyc_status('rwu1dgaUq8DCj3ZLFXzRbc1Aco5xLykMMQ')
```

Returns [`<str of PossibleKycStatuses>`](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/xumm/resource/types/meta/kyc_status_response.py#L66).

###### Notes on KYC information

- Once an account has successfully completed the XUMM KYC flow, the KYC flag will be applied to the account even if the identity document used to KYC expired. The flag shows that the account was **once** KYC'd by a real person with a real identity document.
- Please note that the KYC flag provided by XUMM can't be seen as a "all good, let's go ahead" flag: it should be used as **one of the data points** to determine if an account can be trusted. There are situations where the KYC flag is still `True`, but an account can no longer be trusted. Eg. when account keys are compromised and the account is now controlled by a 3rd party. While unlikely, depending on the level of trust required for your application you may want to mitigate against these kinds of fraud.

##### sdk.get_transaction()

The `get_transaction` method allows you to get the transaction outcome (mainnet)
live from the XRP ledger, as fetched for you by the XUMM backend.

**Note**: it's best to retrieve these results **yourself** instead of relying on the XUMM platform to get live XRPL transaction information! You can use the **[xrpl-py](https://pypi.org/project/xrpl-py)** package to do this:  
[![python version](https://badge.fury.io/py/xrpl-py.svg)](https://pypi.org/project/xrpl-py)

```python
tx_info = sdk.get_transaction(tx_hash)
```

Returns: [`<XrplTransaction>`](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/xumm/resource/types/meta/xrpl_transaction.py#L114).

#### App Storage

App Storage allows you to store a JSON object at the XUMM API platform, containing max 60KB of data.
Your XUMM APP storage is stored at the XUMM API backend, meaning it persists until you overwrite or delete it.

This data is private, and accessible only with your own API credentials. This private JSON data can be used to store credentials / config / bootstrap info / ... for your headless application (eg. POS device).

```python
storage_set = await sdk.storage.set({name: 'Wietse', age: 32, male: True})
print(storage_set)
# True
```

```python
storage_get = sdk.storage.get()
print(storage_get)
# { 'name': 'Wietse', 'age': 32, 'male': True }
```

```python
storage_delete = sdk.storage.delete()
print(storage_delete)
# True
```

```python
storage_get_after_delete = sdk.storage.get()
print(storage_get_after_delete)
# None
```

#### Payloads

##### Intro

Payloads are the primary reason for the XUMM API (thus this SDK) to exist. The [XUMM API Docs explain '**Payloads**'](https://xumm.readme.io/docs/introduction) like this:

>  An XRPL transaction "template" can be posted to the XUMM API. Your transaction tample to sign (so: your "sign request") will be persisted at the XUMM API backend. We now call it a  a **Payload**. XUMM app user(s) can open the Payload (sign request) by scanning a QR code, opening deeplink or receiving push notification and resolve (reject or sign) on their own device.

A payload can contain an XRPL transaction template. Some properties may be omitted, as they will be added by the XUMM app when a user signs a transaction. A simple payload may look like this:

```python
payload = {
  'txjson': {
    'TransactionType' : 'Payment',
    'Destination' : 'rwiETSee2wMz3SBnAG8hkMsCgvGy9LWbZ1',
    'Amount': '1337'
  }
}
```

As you can see the payload looks like a regular XRPL transaction, wrapped in an `txjson` object, omitting the mandatory `Account`, `Fee` and `Sequence` properties. They will be added containing the correct values when the payload is signed by an app user.

Optionally (besides `txjson`) a payload can contain these properties ([PY definition](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/xumm/resource/types/xumm_api/__init__.py#L836)):

- `options` to define payload options like a return URL, expiration, etc.
- `custom_meta` to add metadata, user insruction, your own unique ID, ...
- `user_token` to push the payload to a user (after [obtaining a user specific token](https://xumm.readme.io/docs/pushing-sign-requests))

A more complex payload [could look like this](https://gist.github.com/WietseWind/ecdfd58bece14e5d15e41138fa4b0f4a). A [reference for payload options & custom meta](https://xumm.readme.io/reference/post-payload) can be found in the [API Docs](https://xumm.readme.io/reference/post-payload).

Instead of providing a `txjson` transaction, a transaction formatted as HEX blob (string) can be provided in a `txblob` property.

##### sdk.payload.get

```python
sdk.payload.get(
  payload: Union[str, CreatedPayload],
  return_errors: bool = False
): -> XummPayload
```

To get payload details, status and if resolved & signed: results (transaction, transaction hash, etc.) you can `get()` a payload.

Note! Please don't use _polling_! The XUMM API offers Webhooks (configure your Webhook endpoint in the [Developer Console](https://apps.xumm.dev)) or use [a subscription](#payload-subscriptions-live-updates) to receive live payload updates (for non-SDK users: [Webhooks](https://xumm.readme.io/docs/payload-status)).

You can `get()` a payload by:

- Payload UUID  
  ```python
  payload = sdk.payload.get('aaaaaaaa-bbbb-cccc-dddd-1234567890ab')
  ```

- Passing a created Payload object (see: [sdk.payload.create](#sdkpayloadcreate))  
  ```python
  new_payload: xumm_types.created_payload = {txjson: {...}}
  created = sdk.payload.create(new_payload)
  payload = sdk.payload.get(created)
  ```

If a payload can't be fetched (eg. doesn't exist), `None` will be returned, unless a second param (boolean) is provided to get the SDK to throw an Error in case a payload can't be retrieved:

```python
sdk.payload.get('aaaaaaaa-bbbb-cccc-dddd-1234567890ab', True)
```

##### sdk.payload.create

```python
sdk.payload.create (
payload: create_payload,
return_errors: bool = False
): -> Union[CreatedPayload, None]
```

To create a payload, a `txjson` XRPL transaction can be provided. Alternatively, a transaction formatted as HEX blob (string) can be provided in a `txblob` property. **See the [intro](#intro) for more information about payloads.** Take a look at the [Developer Docs for more information about payloads](https://xumm.readme.io/docs/your-first-payload).

The response (see: [Developer Docs](https://xumm.readme.io/docs/payload-response-resources)) of a `sdk.payload.create()` operation, a `<CreatedPayload>` json object, looks like this:

```json
{
  "uuid": "1289e9ae-7d5d-4d5f-b89c-18633112ce09",
  "next": {
  "always": "https://xumm.app/sign/1289e9ae-7d5d-4d5f-b89c-18633112ce09",
  "no_push_msg_received": "https://xumm.app/sign/1289e9ae-7d5d-4d5f-b89c-18633112ce09/qr"
},
  "refs": {
  "qr_png": "https://xumm.app/sign/1289e9ae-7d5d-4d5f-b89c-18633112ce09_q.png",
  "qr_matrix": "https://xumm.app/sign/1289e9ae-7d5d-4d5f-b89c-18633112ce09_q.json",
  "qr_uri_quality_opts": [ "m", "q", "h" ],
  "websocket_status": "wss://xumm.app/sign/1289e9ae-7d5d-4d5f-b89c-18633112ce09"
},
  "pushed": true
}
```

The `next.always` URL is the URL to send the end user to, to scan a QR code or automatically open the XUMM app (if on mobile). If a `user_token` has been provided as part of the payload data provided to `sdk.payload.create()`, you can see if the payload has been pushed to the end user. A button "didn't receive a push notification" could then take the user to the `next.no_push_msg_received` URL.

Alternatively user routing / instruction flows can be custom built using the QR information provided in the `refs` object, and a subscription for live status updates (opened, signed, etc.) using a WebSocket client can be setup by conneting to the `refs.websocket_status` URL. **Please note: this SDK already offers subscriptions. There's no need to setup your own WebSocket client, see [Payload subscriptions: live updates](#payload-subscriptions-live-updates).** There's more information about the [payload workflow](https://xumm.readme.io/docs/payload-workflow) and a [payload lifecycle](https://xumm.readme.io/docs/doc-payload-life-cycle) in the Developer Docs.

##### sdk.payload.cancel

```python
sdk.payload.cancel(
  payload: Union[str, XummPayload, CreatedPayload],
  return_errors: bool = False
): -> Union[DeletedPayload, None]
```

To cancel a payload, provide a payload UUID (string), a `<XummPayload>` (by performing a `sdk.payload.get()` first) or a `<CreatedPayload>` (by using the response of a `sdk.payload.create()` call). By cancelling an existing payload, the payload will be marked as expired and can no longer be opened by users. 

**Please note**: *if a user already opened the payload in XUMM APP, the payload cannot be cancelled: the user may still be resolving the payload in the XUMM App, and should have a chance to complete that process*.

A response (generic API types [here](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/xumm/resource/types/xumm_api/__init__.py)) looks like:
```python
response.result.cancelled  # bool
response.result.reason  # XummCancelReason
response.meta  # XummPayloadMeta
response.custom_meta  # XummCustomMeta
```

#### Payload subscriptions: live updates

To subscribe to live payload status updates, the XUMM SDK can setup a WebSocket connection and monitor live status events. Emitted events include:

- The payload is opened by a XUMM App user (webpage)
- The payload is opened by a XUMM App user (in the app)
- Payload expiration updates (remaining time in seconds)
- The payload was resolved by rejecting
- The payload was resolved by accepting (signing)

More information about the status update events & sample event data [can be found in the Developer Docs](https://xumm.readme.io/docs/payload-status).

Status updates can be processed by providing a *callback function* to the `sdk.payload.subscribe()` method. Alternatively, the (by the `sdk.payload_subscribe()` method) returned raw websocket can be used to listen for WebSocket `onmessage` events.

The subscription will be closed by either:

- Returning non-void in the *callback function* passed to the `sdk.payload.subscribe()` method
- Manually calling `<PayloadSubscription>.resolve()` on the object returned by the `sdk.payload.subscribe()` method

##### sdk.payload.subscribe

```python
sdk.payload.subscribe(
  payload: Union[str, XummPayload, CreatedPayload],
  callback: on_payload_event
): -> PayloadSubscription
```

If a callback function is not provided, the subscription will stay active until the `<PayloadSubscription>.resolve()` method is called manually, eg. based on handling `<PayloadSubscription>.websocket.onmessage` events.

When a callback function is provided, for every paylaod specific event the callback function will be called with [`<SubscriptionCallbackParams>`](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/xumm/resource/types/payload/subscription_callback_params.py). The `<SubscriptionCallbackParams>.data` property contains parsed JSON containing event information. Either by calling `<SubscriptionCallbackParams>.resolve()` or by returning a non-void value in the *callback function* the subscription will be ended, and the `<PayloadSubscription>.resolved` promise will resolve with the value returned or passed to the `<SubscriptionCallbackParams>.resolve()` method.

Resolving (by returning non-void in the callback or calling `resolve()` manually) closes the WebSocket client the XUMM SDK sets up 'under the hood'.

The [`<PayloadSubscription>`](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/xumm/resource/types/payload/payload_subscription.py) object looks like this:

```python
response.payload  # XummPayload
response.resolved  # Union[CallbackPromise, None]
response.resolve  # CallbackPromise
response.websocket  # WSClient
```

Examples:

- [Async process after returning data in the callback function](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/samples/ws/async_callback.py)
- [Await based on returning data in the callback function](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/samples/ws/await_callback.py)
- [Await based on resolving a callback event](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/samples/ws/await_event.py)
- [Await based on resolving without using a callback function](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/samples/ws/await_no_callback.py)

##### sdk.payload.create_subscribe

```python
sdk.payload.create_and_subscribe(
  payload: CreatePayload,
  callback: on_payload_event
): -> PayloadAndSubscription
```

The [`<PayloadAndSubscription>`](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/xumm/resource/types/payload/payload_and_subscription.py) object is basically a [`<PayloadSubscription>`](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/xumm/resource/types/payload/payload_subscription.py) object with the created payload results in the `created` property:

All information that applies on [`sdk.payload.create()`](#sdkpayloadcreate) and [`sdk.payload.create_and_subscribe()`](#sdkpayloadsubscribe) applies. Differences are:

1. The input for a `sdk.payload.create_and_subscribe()` call isn't a payload UUID / existing payload, but a paykiad to create. 
2. The response object also contains (`<PayloadAndSubscription>.created`) the response obtained when creating the payload

## Debugging (logging)

The XUMM SDK will emit debugging info when invoked with a debug environment variable configured like: `DEBUG=xumm-sdk*` 

You'll see the XUMM SDK debug messages if you invoke your script instead of this:

```
python3 main.py
```

like this:

```
DEBUG=xumm-sdk* python3 main.py
```

## Development

Please note: you most likely just want to **use** the XUMM SDK, to do so, fetch the `xumm-sdk-py` package from PIPI using `pip install xumm-sdk-py`.

If you actually want to change/test/develop/build/contribute (to) the source of the XUMM SDK:

##### Local Build

Please note: at least Python version **3.6+** is required!

To build the code, run `python setup.py install`.

##### Lint & test

Lint the code using `python3 -m flake8 --output-file=./logs/linter.txt --exclude="./samples/, ./build/, ./dist/, ./tests/"`, run tests (pytest) using `python3 test.py tests/`

##### Run development code

Build, run, show debug output & watch `dist/samples/dev.py`, compiled from `samples/dev.py` using `python3`. The `samples/dev.py` file is **not included by default**.

[Here's a sample `samples/dev.py` file](https://github.com/XRPL-Labs/xumm-sdk-py/blob/main/samples/dev.py).
