# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH


import uvclight

from uvclight import interfaces
from zope.interface import Interface
from fanstatic import Library, Resource
from js.bootstrap import bootstrap_js, bootstrap_css


library = Library('nva.tbskin', 'static')
main_css = Resource(library, 'main.css', depends=[bootstrap_css])
main_js = Resource(library, 'main.js', depends=[bootstrap_js])


class TBSkinViewlet(uvclight.Viewlet):
    uvclight.context(Interface)
    uvclight.viewletmanager(interfaces.IHeaders)
    resources = [main_css, main_js]

    def update(self):
        [x.need() for x in self.resources]

    def render(self):
        return u""
