from plone.app.form._named import named_template_adapter
from archetypes.referencebrowserwidget.browser.view  import ReferenceBrowserPopup as ReferenceBrowserPopupOriginal
from zope.component import getMultiAdapter

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.icons.interfaces import IContentIcon
from zope.component import getMultiAdapter


default_popup_template = named_template_adapter(
    ViewPageTemplateFile('templates/popup.pt'))

class ReferenceBrowserPopup(ReferenceBrowserPopupOriginal):
    """ """
    
    def getIcon(self, item):
        """ override original getIcon method"""
        icon = None
        icon = getMultiAdapter((self.context, self.request, item), IContentIcon)
        return icon