# -*- coding: utf-8 -*-

import logging
from Products.Archetypes import atapi
from Products.CMFCore import utils
from collective.pfg.userjoin import config
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.pfg.userjoin')
logger = logging.getLogger('collective.pfg.userjoin')


def initialize(context):
    from collective.pfg.userjoin import content

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
            content_types=(atype, ),
            permission=config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
            ).initialize(context)
