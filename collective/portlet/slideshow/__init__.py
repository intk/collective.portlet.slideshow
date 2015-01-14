from zope.i18nmessageid import MessageFactory
PloneMessageFactory = MessageFactory('plone')

from Products.CMFCore.permissions import setDefaultRoles

PROJECTNAME = "collective.portlet.slideshow"
DEFAULT_ADD_CONTENT_PERMISSION = "%s: Add collection portlet" % PROJECTNAME

setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION,
                ('Manager', 'Site Administrator', 'Owner',))

