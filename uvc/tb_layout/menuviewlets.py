# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import uvclight


from uvc.tb_layout import interfaces
from zope.interface import Interface
from zope.component import getMultiAdapter
from dolmen.viewlet.interfaces import IViewletManager


class GlobalMenuViewlet(uvclight.Viewlet):
    uvclight.viewletmanager(interfaces.IPageTop)
    uvclight.context(Interface)
    uvclight.order(20)

    def update(self):
        self.menu = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'globalmenu')
        self.menu.update()

    def render(self):
        return self.menu.render()


class FooterViewlet(uvclight.Viewlet):
    uvclight.viewletmanager(interfaces.IFooter)
    uvclight.context(Interface)
    uvclight.order(10)

    def update(self):
        self.menu = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'footermenu')
        self.menu.update()

    def render(self):
        return self.menu.render()


class PersonalPreferencesViewlet(uvclight.Viewlet):
    uvclight.viewletmanager(interfaces.IPageTop)
    uvclight.context(Interface)
    uvclight.order(40)

    def update(self):
        self.menu = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'personalpreferences')
        self.menu.update()

    def render(self):
        return self.menu.render()


class DocumentActionsMenuViewlet(uvclight.Viewlet):
    uvclight.viewletmanager(interfaces.IAboveContent)
    uvclight.context(Interface)
    uvclight.order(40)

    def update(self):
        self.menu = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'documentactions')
        self.menu.update()

    def render(self):
        return self.menu.render()


class ContextualActionsMenuViewlet(uvclight.Viewlet):
    uvclight.viewletmanager(interfaces.IAboveContent)
    uvclight.context(Interface)
    uvclight.order(50)

    def update(self):
        self.menu = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IViewletManager, 'contextualactionsmenu')
        self.menu.update()

    def render(self):
        return self.menu.render()
