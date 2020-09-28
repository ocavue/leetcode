def logger(func):
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)

        print_args = ", ".join([repr(a) for a in args])
        print_kwargs = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        print_all = ", ".join([p for p in [print_args, print_kwargs] if p])
        print(f"{func.__name__}({print_all}) == {result}")
        return result

    return new_func
