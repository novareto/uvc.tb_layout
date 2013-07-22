# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


from dolmen.menu.interfaces import IMenu
from dolmen.viewlet.interfaces import IViewSlot


#
### Viewlet Managers
#


class IPageTop(IViewSlot):
    """Marker For the area that sits at the top of the page.
    """


class ITabs(IViewSlot):
    """Marker for the action tabs.
    """


class IAboveContent(IViewSlot):
    """Marker For the area that sits above the page body.
    """


class IBelowContent(IViewSlot):
    """Marker For the area that sits under the page body.
    """


class IHeaders(IViewSlot):
    """Marker For Headers
    """


class IToolbar(IViewSlot):
    """Marker for Toolbar
    """


class IFooter(IViewSlot):
    """ """


#
### Menus
#


class IGlobalMenu(IMenu):
    """Marker for GlobalMenu
    """


class IPersonalPreferences(IMenu):
    """Marker for PersonalPreferences
    """


class IFooterMenu(IMenu):
    """Marker for Footer
    """


class IDocumentActions(IMenu):
    """Marker for DocumentActions
    """


class IExtraViews(IMenu):
    """Marker for additional Views for Folders
       Objects etc...
    """


class IPersonalMenu(IMenu):
    """Marker for PersonalMenu
    """



#
### Maybe Needed
#



#class ISidebar(IMenu):
#    """Marker for Sitebar
#    """
#
#
#class IPanels(IMenu):
#    """Marker interface for the panels display.
#    """
#
#
#class IHelp(IMenu):
#    """Marker for Help
#    """
#
#
#class IExtraInfo(IMenu):
#    """Marker for ExtraInfo in Forms
#    """
#
#class ISpotMenu(IViewSlot):
#    """ Special Menu """
#
#
#class IBeforeActions(IViewSlot):
#    """ Marker Interfae"""
