import time

import droid_do as dd
from Point import Point

class Reel(object):
    """
        Reel page
    """

    def __init__(self, index):
        self.index = index
        self.like_button = Point(673, 793)
        self.comment_button = Point(675, 911)
        self.send_button = Point(675, 979)
        self.account_button = Point(105, 1193)

    def click_like_button(self):
        dd.click_point(self.like_button, self.index)
        time.sleep(1)

    def click_comment_button(self):
        dd.click_point(self.comment_button, self.index)
        time.sleep(1)

    def click_send_button(self):
        dd.click_point(self.send_button, self.index)
        time.sleep(1)

    def click_go_to_account_page(self):
        dd.click_point(self.account_button, self.index)
        time.sleep(1)

    def watch_reel(self, duration=30):
        time.sleep(duration)

    def next_reel(self):
        dd.swipe(1000, 300, 500, 300, self.index)
