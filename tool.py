import unittest


def logger(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)

        print_args = ", ".join([repr(a) for a in args])
        print_kwargs = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        print_all = ", ".join([p for p in [print_args, print_kwargs] if p])
        print(f"{func.__name__}({print_all}) == {result}")
        return result

    return new_func


def test():
    return unittest.TestCase("__init__")


def t(received, expected):
    assert (expected) == (received), "expected: {}, received: {}".format(expected, received)


def tt(func):
    def assert_equal(input_args, expected_result):
        if isinstance(input_args, list):
            received_result = func(*input_args)
        elif isinstance(input_args, tuple):
            received_result = func(*input_args)
        elif isinstance(input_args, dict):
            received_result = func(**input_args)
        else:
            raise Exception(f"unknow input_args type {type(input_args)}")

        t(received_result, expected_result)

    return assert_equal
