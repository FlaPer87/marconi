# Copyright (c) 2013 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import simplejson as json


class MalformedJSON(ValueError):
    """JSON string is not valid."""
    pass


def read_json(stream, len):
    """Like json.load, but converts ValueError to MalformedJSON upon failure.

    :param stream: a file-like object
    :param len: the number of bytes to read from stream
    """
    try:
        return json.loads(stream.read(len))

    except ValueError as ex:
        raise MalformedJSON(ex)


def to_json(obj):
    """Like json.dumps, but outputs a UTF-8 encoded string.

    :param obj: a JSON-serializable object
    """
    return json.dumps(obj, ensure_ascii=False)


def purge(src):
    """Returns a copy of a dict, excluding any keys set to `None`.

    :param src: a dictionary-like object to copy
    """
    return dict([(k, v) for k, v in src.items() if v is not None])
