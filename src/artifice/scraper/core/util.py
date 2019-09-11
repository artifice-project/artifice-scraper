def get_package_name():
    import inspect
    try:
        pkg = inspect.getmodule(inspect.stack()[1][0]).__name__
        return pkg.split('.')[0]
    except AttributeError as err:
        raise AttributeError('{0}\nFunction must be called from within another module to return a valid result'.format(str(err)))
