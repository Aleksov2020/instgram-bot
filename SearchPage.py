import time

import droid_do as dd


class SearchPage(object):
    def __init__(self, index):
        self.index = index
        self.x_search_field = 325
        self.y_search_field = 73
        self.x_first_result = 227
        self.y_first_result = 297

    def click_search_field(self):
        dd.click(self.x_search_field, self.y_search_field, self.index)
        time.sleep(1)

    def click_first_result(self):
        dd.click(self.x_first_result, self.y_first_result, self.index)
        time.sleep(1)

    # TODO add go to reccs