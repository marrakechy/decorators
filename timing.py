import time
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        time_elapsed = start - end

        print(f"{func.__name__} took {time_elapsed:.4f} seconds to execute")
        return result

    return wrapper

