pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
functionsdir = join_paths(pkgdatadir, 'shardsctl/functions')

shardsctl_sources = [
    '__init__.py',
    'rebase.py'
]

install_data(shardsctl_sources, install_dir: functionsdir)