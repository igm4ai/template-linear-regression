from igm.conf import igm_project, cpy


def info():
    print('This is the project of linear regression.')
    print('The function is y = {{ user.k }}x + {{ user.b }}')


igm_project(
    name='linear-regression-demo',
    version='0.0.1',
    template_name={{template.name | potc}},
    template_version={{template.version | potc}},
    created_at={{py.time.time() | potc}},
    scripts={
        None: cpy('main.py'),
        'info': info,
    }
)
