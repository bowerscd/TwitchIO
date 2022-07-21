"""
The MIT License (MIT)

Copyright (c) 2017-present TwitchIO

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import datetime
import time
from typing import TYPE_CHECKING, Union
from .enums import UserNoticeType
from .message import Message
from .channel import Channel
from .chatter import Chatter


class UserNotice:

    """
    Attributes
    -----------

    """

    __slots__ = (
        "_message",
        "_author",
        "_tags",
        "_channel",
        "_raw_data",
        "_id",
        "_timestamp",
        "_notice_type"
    )

    __type_lookup__ = { x.value: x for x in UserNoticeType }

    def __init__(self, **kwargs):
        self._message = kwargs.get("message")
        self._author = kwargs.get("author")
        self._tags = kwargs.get("tags")
        self._channel = kwargs.get("channel")
        self._raw_data = kwargs.get("raw_data")

        try:
            self._id = self._tags["id"]
            self._timestamp = self._tags["tmi-sent-ts"]
            self._notice_type = UserNotice.__type_lookup__.get(self._tags["msg-id"])
        except KeyError:
            self._id = None
            self._timestamp = datetime.datetime.now().timestamp() * 1000
            self._notice_type = None

    @property
    def message(self) -> Message | None:
        return self._message

    @property
    def channel(self) -> Channel:
        return self._channel
    
    @property
    def tags(self) -> dict:
        return self._tags

    @property
    def author(self) -> Chatter:
        return self._author

    @property
    def notice_type(self) -> UserNoticeType | None:
        return self._notice_type
