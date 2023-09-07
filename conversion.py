def convert(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):
            return result
        try:
            return int(result)
        except ValueError:
            try:
                return float(result)
            except ValueError:
                raise ValueError("Cannot convert the result to an integer or flaot number")
    return wrapper

@convert
def return_something(value):
    return value

result = return_something(839.2)

print(result)


#Im stuck on this, does not work, I tried the consol too
