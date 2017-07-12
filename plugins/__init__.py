def load_plugins(plugins_dir = 'plugins'):
    plugins_list = dict()
    import pkgutil
    plugins = __import__(plugins_dir)
    for importer, package_name, _ in pkgutil.iter_modules(plugins.__path__):
        module = importer.find_module(package_name).load_module('%s.%s' % (plugins_dir, package_name))
        if hasattr(module, 'command'):
            plugins_list[package_name] = dict(
                    command = getattr(module, 'command'),
                    help_text = getattr(module, 'help_text', None)
                    )

    return plugins_list
