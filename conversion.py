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

