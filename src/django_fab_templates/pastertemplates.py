from paste.script.templates import Template
from paste.script.templates import var
from random import choice

class DjangoTemplate(Template):

    vars = [
    ]

    use_cheetah = True
    required_templates = []

    def check_vars(self, vars, command):
        if not command.options.no_interactive and \
           not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return super(DjangoTemplate, self).check_vars(vars, command)

def append_secret_key(vars):
    default_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    vars.append(
        var('secret_key', 'Secret key', default=default_key)
    )

def append_db_password(vars):
    default_key = ''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(10)])
    vars.append(
        var('db_password', 'DB Password', default=default_key)
    )


class VagrantTemplate(DjangoTemplate):
    _template_dir = 'templates/vagrant_project'
    summary = 'Template for a Django project that could be deployed to vagrant-managed vitrual box'
    
    def __init__(self, name):
        append_secret_key(self.vars)
        append_db_password(self.vars)
        super(VagrantTemplate, self).__init__(name)
        
