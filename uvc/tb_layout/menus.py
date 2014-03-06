# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import uvclight
from cromlech.browser import ITemplate
from dolmen.menu.interfaces import IMenu, IMenuEntry
from grokcore.component import adapter, implementer
from uvclight import interfaces
from zope.interface import Interface


class GlobalMenu(uvclight.Menu):
    uvclight.implements(interfaces.IGlobalMenu)
    uvclight.name('globalmenu')
    css = "nav navbar-nav"

    def render(self):
        return uvclight.Menu.render(self)
    
    
class FooterMenu(uvclight.Menu):
    uvclight.implements(interfaces.IFooterMenu)
    uvclight.name('footermenu')
    css = "nav nav-tabs pull-right"


class PersonalPreferences(uvclight.Menu):
    uvclight.implements(interfaces.IPersonalPreferences)
    uvclight.name('personalpreferences')
    css = "nav navbar-nav pull-right"


class DocumentActionsMenu(uvclight.Menu):
    uvclight.implements(interfaces.IDocumentActions)
    uvclight.name('documentactions')
    css = "pull-right"


class ExtraViews(uvclight.Menu):
    uvclight.implements(interfaces.IExtraViews)
    uvclight.name('extraviews')


class PersonalMenu(uvclight.Menu):
    uvclight.implements(interfaces.IPersonalMenu)
    uvclight.name('personalmenu')


class ContextualActionsMenu(uvclight.ContextualActionsMenu):
    css = "nav pull-right"
    template = uvclight.get_template('contextualactionsmenu.cpt', __file__)


@adapter(IMenu, Interface)
@implementer(ITemplate)
def menu_template(context, request):
    """default template for the menu"""
    return uvclight.get_template('menu.cpt', __file__)


@adapter(IMenuEntry, Interface)
@implementer(ITemplate)
def entry_template(context, request):
    """default template for a menu entry"""
    return uvclight.get_template('entry.cpt', __file__)
