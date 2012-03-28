from collective import dexteritytextindexer
from plone.directives import form
from plone.app.textfield import RichText
from Products.CMFPlone import PloneMessageFactory as _

class IDocument(form.Schema):

    dexteritytextindexer.searchable('text')
    text = RichText(
        title = _(u'label_body_text', default=u'Body Text'),
        required = False
        )

