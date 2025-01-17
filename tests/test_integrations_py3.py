import asyncio
from datetime import timedelta

import pytest
from tornado import gen
from tornado import ioloop

from aspectlib import PY37plus
from aspectlib import debug

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


@pytest.mark.skipif(PY37plus, reason="Test is incompatible with PEP-479")
def test_decorate_asyncio_coroutine():
    buf = StringIO()

    @asyncio.coroutine
    @debug.log(print_to=buf, module=False, stacktrace=2, result_repr=repr)
    def coro():
        yield from asyncio.sleep(0.01)
        return "result"

    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro())
    output = buf.getvalue()
    assert 'coro => %r' % 'result' in output


def test_decorate_tornado_coroutine():
    buf = StringIO()

    @gen.coroutine
    @debug.log(print_to=buf, module=False, stacktrace=2, result_repr=repr)
    def coro():
        if hasattr(gen, 'Task'):
            yield gen.Task(loop.add_timeout, timedelta(microseconds=10))
        else:
            yield gen.sleep(0.01)
        return "result"

    loop = ioloop.IOLoop.current()
    loop.run_sync(coro)
    output = buf.getvalue()
    assert 'coro => %r' % 'result' in output
