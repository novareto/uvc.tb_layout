# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import uvclight

from uvc.tb_layout import interfaces
from zope.interface import Interface


class Headers(uvclight.ViewletManager):
    """Viewlet Manager for the Header
    """
    uvclight.name('uvc-headers')
    uvclight.context(Interface)
    uvclight.implements(interfaces.IHeaders)


class PageTop(uvclight.ViewletManager):
    """ViewletManager for the PageTop
    """
    uvclight.name('uvc-pagetop')
    uvclight.context(Interface)
    uvclight.implements(interfaces.IPageTop)


class AboveContent(uvclight.ViewletManager):
    uvclight.name('uvc-above-body')
    uvclight.context(Interface)
    uvclight.implements(interfaces.IAboveContent)


class BelowContent(uvclight.ViewletManager):
    uvclight.name('uvc-below-body')
    uvclight.context(Interface)
    uvclight.implements(interfaces.IBelowContent)


class Footer(uvclight.ViewletManager):
    """ViewletManager for the PageTop
    """
    uvclight.name('uvc-footer')
    uvclight.context(Interface)
    uvclight.implements(interfaces.IFooter)
