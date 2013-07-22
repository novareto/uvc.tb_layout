# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


import uvclight
from zope.interface import Interface


class Layout(uvclight.Layout):
    uvclight.context(Interface)

    template = uvclight.get_template('layout.cpt', __file__)
    base = "/"
