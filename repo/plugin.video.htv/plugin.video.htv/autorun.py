# -*- coding: utf-8 -*-

import xbmc, xbmcaddon

addon = xbmcaddon.Addon(id='plugin.video.htv')

Auto_mode = addon.getSetting('auto_mode')

if Auto_mode == 'true':				
    xbmc.executebuiltin("RunAddon(plugin.video.htv)")