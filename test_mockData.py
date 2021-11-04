#!/usr/bin/python

"""Setting up unit testing for the mockData module."""

import pytest
import mockData

def test_fakeIt():
    errors = []

    valueToTest = mockData.fakeIt("boolean")

    if valueToTest == 1:
        pass
    elif valueToTest == 0:
        pass
    else:
        errors.append("fakeIt('boolean') returns a bad value: %s".format(str(valueToTest)))

    assert not errors, "Found errors:\n{}".format("\n".join(errors))
