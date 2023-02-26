import time

import droid_do as dd

from Utils.Point import Point


class SearchPage(object):
    def __init__(self, index):
        self.index = index
        self.search_field = Point(325, 73)
        self.first_result = Point(227, 297)

    def click_search_field(self):
        dd.click_point(self.search_field, self.index)
        time.sleep(1)

    def click_first_result(self):
        dd.click_point(self.first_result, self.index)
        time.sleep(1)

    # TODO add go to reccs
