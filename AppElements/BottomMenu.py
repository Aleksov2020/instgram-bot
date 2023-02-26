import time

import droid_do as dd


class BottomMenu(object):
    """
        start page, bottom menu
    """
    def __init__(self, index):
        self.index = index
        self.x_home = 73
        self.y_home = 1247
        self.x_search = 217
        self.y_search = 1247
        self.x_add = 363
        self.y_add = 1247
        self.x_reel = 503
        self.y_reel = 1247
        self.x_profile = 653
        self.y_profile = 1247

    def click_home(self):
        dd.click(self.x_home, self.y_home, self.index)
        time.sleep(1)

    def click_search(self):
        dd.click(self.x_search, self.y_search, self.index)
        time.sleep(1)

    def click_add(self):
        dd.click(self.x_add, self.y_add, self.index)
        time.sleep(1)

    def click_reel(self):
        dd.click(self.x_reel, self.y_reel, self.index)
        time.sleep(1)

    def click_profile(self):
        dd.click(self.x_profile, self.y_profile, self.index)
        time.sleep(1)
