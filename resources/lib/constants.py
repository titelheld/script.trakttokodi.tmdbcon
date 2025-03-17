# -*- coding: utf-8 -*-
"""
     
    Copyright (C) 2016 anxdpanic
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import kodi
from url_dispatcher import URL_Dispatcher
from enum import Enum


class Modes(Enum):
    MAIN = 'main'
    PLAY = 'play'
    OPEN = 'open'
    TMDB_HELPER_PLAY = 'tmdb_helper_play'
    TMDB_HELPER_BROWSE = 'tmdb_helper_browse'


class Directories(Enum):
    DATA = kodi.translate_path(f'special://profile/addon_data/{kodi.get_id()}/')


class Icons(Enum):
    ADDON = kodi.translate_path(f'special://home/addons/{kodi.get_id()}/icon.png')


DISPATCHER = URL_Dispatcher()
