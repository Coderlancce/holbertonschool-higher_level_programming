#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr, exc_info

    try:
        return fct(*args)
    except Exception as err:
        stderr.write("Exception: {}\n".format(err))
