import time

import droid_do as dd

from Point import Point


class SendMenu(object):
    def __init__(self, index):
        self.index = index
        self.search_field = Point(197, 443)
        self.send_reel_to_story = Point(225, 525)
        self.add_text = Point(271, 365)
        self.first_result = Point(160, 613)
        self.send_message_first_result = Point(581, 617)

    def click_search_field(self):
        dd.click_point(self.search_field, self.index)
        time.sleep(1)

    def click_send_reel_to_story(self):
        dd.click_point(self.send_reel_to_story, self.index)
        time.sleep(1)

    def click_add_text(self):
        dd.click_point(self.add_text, self.index)
        time.sleep(1)

    def click_first_result(self):
        dd.click_point(self.first_result, self.index)
        time.sleep(1)

    def click_first_result(self):
        dd.click_point(self.first_result, self.index)
        time.sleep(1)

    def click_send_message_first_result(self):
        dd.click_point(self.send_message_first_result, self.index)
        time.sleep(1)