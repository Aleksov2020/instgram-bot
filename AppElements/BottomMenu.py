import time

import droid_do as dd
from Utils.Point import Point

class BottomMenu(object):
    """
        start page, bottom menu
    """
    def __init__(self, index):
        self.index = index
        self.home = Point(73, 1247)
        self.search = Point(217, 1247)
        self.add = Point(363, 1247)
        self.reel = Point(503, 1247)
        self.profile = Point(653, 2147)

    def click_home(self):
        dd.click_point(self.home, self.index)
        time.sleep(1)

    def click_search(self):
        dd.click_point(self.search, self.index)
        time.sleep(1)

    def click_add(self):
        dd.click_point(self.add, self.index)
        time.sleep(1)

    def click_reel(self):
        dd.click_point(self.reel, self.index)
        time.sleep(1)

    def click_profile(self):
        dd.click_point(self.profile, self.index)
        time.sleep(1)
