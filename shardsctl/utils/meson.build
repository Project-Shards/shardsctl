kgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
utilsdir = join_paths(pkgdatadir, 'shardsctl/utils')

shardsctl_sources = [
    '__init__.py',
    'log.py'
]

install_data(shardsctl_sources, install_dir: utilsdir)