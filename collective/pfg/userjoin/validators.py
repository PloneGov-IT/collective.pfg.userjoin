# -*- coding: utf-8 -*-

from zope.interface import implements
from Products.validation.interfaces.IValidator import IValidator
from Products.validation import validation
from collective.pfg.userjoin import _
from Products.PloneFormGen import config as pfg_config


class IsValidUseridValidator(object):
    """Check if a string is a valid userid"""

    implements(IValidator)

    name = 'IsValidUseridValidator'

    def __init__(self, name, title='', description=''):
        self.name = name
        self.title = title or name
        self.description = description

    def __call__(self, value, *args, **kwargs):
        # TODO: to be finished
        return True
        return ("Validation failed (%s): is not a valid username." % self.name)

validation.register(IsValidUseridValidator('isValidUserid'))

pfg_config.stringValidators += (
    {'id':'isValidUserid',
     'i18nid':'vocabulary_isvaliduserid_text',
     'title':u'Is a valid userid',
     'errmsg':u'This userid is invalid or already in use',
     'errid':'pfg_isValidUserid'
     },)
