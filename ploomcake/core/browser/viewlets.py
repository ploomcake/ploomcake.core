from Acquisition import aq_base, aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from zope.component import getMultiAdapter
from zope.security import checkPermission
from plone.registry.interfaces import IRegistry
from plone.app.layout.navigation.defaultpage import isDefaultPage
from Products.LinguaPlone.browser.selector import TranslatableLanguageSelector as OriginalLanguageSelector
from ploomcake.core import _

class DefaultViewDisclaimerViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/defaultviewdisclaimer_viewlet.pt')
    
    def __init__(self, context, request, view, manager=None):
        super(DefaultViewDisclaimerViewlet, self).__init__(context, request, view, manager)
        registry = getUtility(IRegistry)
        self.message = _('Click here to change the container\'s workflow state')
        self.visible = False
        self.container = self.context.aq_parent

    def update(self):
        is_default_page = isDefaultPage(self.container, self.context)
        can_review = checkPermission('cmf.ReviewPortalContent', self.container)
        if is_default_page and can_review:
            wftool = getToolByName(self.context,'portal_workflow')
            if len(wftool.getChainFor(self.context)) and len(wftool.getChainFor(self.container)):
                page_wf_state = len(wftool.getChainFor(self.context)) and wftool.getInfoFor(self.context, 'review_state')
                container_wf_state = wftool.getInfoFor(self.container, 'review_state')
                self.visible = page_wf_state != container_wf_state

class ContentReverseRelatedItems(ViewletBase):

    index = ViewPageTemplateFile("templates/document_reverserelateditems.pt")

    def related_items(self):
        if hasattr(self.context, 'getBRefs'):
            referrers = [item for item in self.context.getBRefs('relatesTo') if checkPermission('zope2.View', item)] 
        else:
            referrers = []
        return referrers


class LanguageSelector(OriginalLanguageSelector):
    render = ViewPageTemplateFile("templates/languageselector.pt")
    def first_language(self):
        """ Returns the active language code """
        bound = self.tool.getLanguageBindings()
        current = bound[0]
        if current:
            return self.tool.getAvailableLanguageInformation()[current]
        return 
