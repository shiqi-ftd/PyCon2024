def log_args(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

def call_with_logging(func, *args, **kwargs):
    log_args(*args, **kwargs)
    return func(*args, **kwargs)

def greet(*args, **kwargs):
    return f"{kwargs}!"

result = call_with_logging(greet, "Hello", "Alice", "asd", "asdas")
print(result)
