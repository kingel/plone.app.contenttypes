from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from Products.CMFPlone import PloneMessageFactory as _
from zope import schema

from plone.rfc822.interfaces import IPrimaryField
from zope.interface import alsoProvides

class IImage(form.Schema):
    
    title = schema.TextLine(
        title=_(u'label_title', default=u'Title'),
        required=False,
        )
    
    description = schema.Text(
        title=_(u'label_description', default=u'Description'),
        description=u'',
        required=False,
        )

    form.primary('image')
    image = NamedBlobImage(
        title=_(u'label_image', default=u'Image'),
        required=True,
        )
