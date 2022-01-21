#!/usr/bin/env python
# coding: utf-8

from typing import Union, Callable, Any
from .subscription_callback_params import SubscriptionCallbackParams


def on_payload_event(
    subscriptionCallback: SubscriptionCallbackParams
) -> Union[None, Callable[[Any], Any]]:
    return subscriptionCallback
