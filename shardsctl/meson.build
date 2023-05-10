pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'shardsctl')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('pkgdatadir', pkgdatadir)
configure_file(
            input: 'shardsctl.in',
           output: 'shardsctl',
    configuration: conf,
          install: true,
      install_dir: get_option('bindir'),
     install_mode: 'r-xr--r--'
)

shardsctl_sources = [
    '__init__.py',
    'main.py'
]

subdir('utils')

install_data(shardsctl_sources, install_dir: moduledir)
