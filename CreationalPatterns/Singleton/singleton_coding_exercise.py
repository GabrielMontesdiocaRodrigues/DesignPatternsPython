def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not

    susported_singleton = factory()
    susported_singleton2 = factory()
    
    return susported_singleton is susported_singleton2

