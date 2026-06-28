from collections import OrderedDict

def primary_lru_cache(maxsize: int):

    if maxsize <= 0:
        raise ValueError('maxsize must be positive')

    cache = OrderedDict()
    hits = 0
    misses = 0

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal hits, misses

            key = (args, tuple(sorted(kwargs.items())))

            if key in cache:
                cache.move_to_end(key)
                hits += 1
                print("From cache: ")
                return cache[key]
            else:
                misses += 1
                result = func(*args, **kwargs)
                cache[key] = result

            if len(cache) > maxsize:
                cache.popitem(last = False)

            return result

        def cache_info():
            print(f'hits = {hits}, misses = {misses}, maxsize = {maxsize}, length = {len(cache)}')

        def cache_clear():
            nonlocal hits, misses

            hits = 0
            misses = 0
            cache.clear()

        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear
        
        return wrapper
    
    return decorator

@primary_lru_cache(maxsize = 10)
def power(a, b):
    return a ** b

# for example
print(power(2, 3))
print(power(3, 3))
print(power(2, 7))
print(power(2, 3))
print(power(5, 3))
print(power(3, 3))
print(power(2, 3))

print(power.cache_info())
power.cache_clear()

