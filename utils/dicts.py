def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    """
    if 1 > len(collection):
        return default
    elif key in collection:
        return collection[key]
    else:
        return default
