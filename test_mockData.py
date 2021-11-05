#!/usr/bin/python

"""Setting up unit testing for the mockData module."""

import mockData
import datetime

def test_fakeIt():
    errors = []

    boo = mockData.fakeIt("boolean")
    if boo == 1:
        pass
    elif boo == 0:
        pass
    else:
        errors.append("fakeIt('boolean') returns a bad value: %s".format(str(boo)))
    mockInt = mockData.fakeIt("integer",start=0,end=17)
    if mockInt in range(0,17):
        pass
    else:
        errors.append("fakeIt('integer') returns a bad value: %s".format(str(mockInt)))
    string = mockData.fakeIt("string",length=100)
    if string == None:
        errors.append("fakeIt('string') returns a bad value: %s".format(str(string)))
    else:
        pass
    factor = mockData.fakeIt("factor",description="red|blue|green|yellow")
    if factor in [x for x in "red|blue|green|yellow".split( "|" )]:
        pass
    else:
        errors.append("fakeIt('factor') returns a bad value: %s".format(str(factor)))
    num = mockData.fakeIt("number",start=0,end=17)
    if 0 <= num <= 17:
        pass
    else:
        errors.append("fakeIt('number') returns a bad value: %s".format(str(num)))
    mockName = mockData.fakeIt("name")
    if mockName == None:
        errors.append("fakeIt('name') returns a bad value: %s".format(str(mockName)))
    else:
        pass
    testdate = mockData.fakeIt("date",start="2000-12-12",end="2020-12-12",description="%Y-%m-%d")
    try:
        datetime.datetime.strptime(testdate,"%Y-%m-%d")
    except ValueError:
        errors.append("fakeIt('date') returns a bad value: %s".format(str(testdate)))

    assert not errors, "Found errors:\n{}".format("\n".join(errors))
