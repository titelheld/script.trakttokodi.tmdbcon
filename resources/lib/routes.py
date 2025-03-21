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
import log_utils
from constants import DISPATCHER, MODES

i18n = kodi.i18n
addon_id = 'plugin.video.themoviedb.helper'


@DISPATCHER.register(MODES.MAIN, kwargs=['content_type'])
def main_route(content_type=''):
    kodi.show_settings()


@DISPATCHER.register(MODES.PLAY, args=['video_type', 'title', 'year'], kwargs=['trakt_id', 'episode_id', 'season_id', 'season', 'episode', 'ep_title', 'imdb_id', 'tmdb_id', 'tvdb_id'])
def play_route(video_type, title, year, trakt_id=None, episode_id=None, season_id=None, imdb_id=None, tmdb_id=None, tvdb_id=None, season=None, episode=None, ep_title=None):
    plugin_url = None

    if video_type == 'episode':
        plugin_url = f'plugin://{addon_id}/?action=play&video_type={video_type}&season={season}&episode={episode}&imdb_id={imdb_id}&tmdb_id={tmdb_id}&tvdb_id={tvdb_id}&title={title}&year={year}'

    elif video_type == 'movie':
        plugin_url = f'plugin://{addon_id}/?action=play&video_type={video_type}&imdb_id={imdb_id}&tmdb_id={tmdb_id}&tvdb_id={tvdb_id}&title={title}&year={year}'

    if plugin_url:
        kodi.execute_builtin(f'ActivateWindow(Videos,{plugin_url})')


@DISPATCHER.register(MODES.OPEN, args=['video_type', 'title', 'year'], kwargs=['trakt_id', 'episode_id', 'season_id', 'season', 'episode', 'ep_title', 'imdb_id', 'tmdb_id', 'tvdb_id'])
def open_route(video_type, title, year, trakt_id=None, episode_id=None, season_id=None, imdb_id=None, tmdb_id=None, tvdb_id=None, season=None, episode=None, ep_title=None):
    plugin_url = None

    if video_type == 'episode':
        play_route(video_type, title, year, trakt_id, episode_id, season_id, imdb_id, tmdb_id, tvdb_id, season, episode, ep_title)

    elif video_type == 'movie':
        play_route(video_type, title, year, trakt_id, episode_id, season_id, imdb_id, tmdb_id, tvdb_id, season, episode, ep_title)

    elif video_type == 'season':
        plugin_url = f'plugin://{addon_id}/?action=browse&video_type={video_type}&season={season}&imdb_id={imdb_id}&tmdb_id={tmdb_id}&tvdb_id={tvdb_id}&title={title}&year={year}'

    elif video_type == 'show':
        plugin_url = f'plugin://{addon_id}/?action=browse&video_type={video_type}&imdb_id={imdb_id}&tmdb_id={tmdb_id}&tvdb_id={tvdb_id}&title={title}&year={year}'

    if plugin_url:
        kodi.execute_builtin(f'RunPlugin({plugin_url})')


@DISPATCHER.register(MODES.TMDB_HELPER_PLAY, args=['video_type', 'title', 'year'], kwargs=['imdb_id', 'tmdb_id', 'tvdb_id'])
def tmdb_helper_play_route(video_type, title, year, imdb_id=None, tmdb_id=None, tvdb_id=None):
    plugin_url = f'plugin://{addon_id}/?action=play&video_type={video_type}&imdb_id={imdb_id}&tmdb_id={tmdb_id}&tvdb_id={tvdb_id}&title={title}&year={year}'
    kodi.execute_builtin(f'RunPlugin({plugin_url})')


@DISPATCHER.register(MODES.TMDB_HELPER_BROWSE, args=['video_type', 'title', 'year'], kwargs=['imdb_id', 'tmdb_id', 'tvdb_id'])
def tmdb_helper_browse_route(video_type, title, year, imdb_id=None, tmdb_id=None, tvdb_id=None):
    plugin_url = f'plugin://{addon_id}/?action=browse&video_type={video_type}&imdb_id={imdb_id}&tmdb_id={tmdb_id}&tvdb_id={tvdb_id}&title={title}&year={year}'
    kodi.execute_builtin(f'RunPlugin({plugin_url})')
