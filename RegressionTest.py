#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU LESSER GENERAL PUBLIC LICENSEG as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.
# If not, see <http://www.gnu.org/copyleft/lesser.html>.
#
# RssRead 0.3.2
# by Luca Francesca, 2013

import RssRead as feed
import unittest
import time 
import string

class RegressionTest(unittest.TestCase):

    def setUp(self):
        self.rss = feed.RssRead()

    def test_configuration_loading(self):
        self.assertNotEqual(self.rss._siteConf, {}, 'Problems with configuration loading')

    def test_fmt_loading_sintax(self):
        try:
            self.rss.loadNewsRss('slashdot')
        except feed.FormatError:
            self.fail('Format for news output is invalid')

    def test_loading_news(self):
        try:
            self.rss.loadNewsRss('slashdot')
        except KeyError:
            self.fail('Error loading news, unexpected')

    def test_unicode_except(self):
        try:
            self.rss.loadNewsRss('torrent')
        except (UnicodeEncodeError, KeyError):
            self.fail('Unicode Error thrown, unexpected')

    def test_add_site_twice(self):
        self.rss += 'io', 'tu'
        try:
            self.rss += 'io', 'tu'
        except (TypeError, feed.SiteError):
            self.fail('Already present site exception thrown, expected')

    def test_remove_site_twice(self):
        self.rss -= 'io'
        try:
            self.rss -= 'io'
        except (TypeError, feed.SiteError):
            self.fail('Already removed site exception thrown, expected')

    def test_already_present_site(self):
        try:
            self.rss.loadNewsRss('hwupgrade.it')
        except (TypeError, feed.SiteError):
            self.fail('Site not present exception thrown, expected')


if __name__ == '__main__':
    unittest.main()
