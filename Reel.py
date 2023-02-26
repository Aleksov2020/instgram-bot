import time

import droid_do as dd


class Reel(object):
    """
        Reel page
    """

    def __init__(self, index):
        self.index = index
        self.x_like_button = 673
        self.y_like_button = 793
        self.x_comment_button = 675
        self.y_comment_button = 911
        self.x_send_button = 675
        self.y_send_button = 979
        self.x_account_button = 105
        self.y_account_button = 1193

    def click_like_button(self):
        dd.click(self.x_like_button, self.y_like_button, self.index)
        time.sleep(1)

    def click_comment_button(self):
        dd.click(self.x_comment_button, self.y_comment_button, self.index)
        time.sleep(1)

    def click_send_button(self):
        dd.click(self.x_send_button, self.y_send_button, self.index)
        time.sleep(1)

    def click_go_to_account_page(self):
        dd.click(self.x_account_button, self.y_account_button, self.index)
        time.sleep(1)

    def watch_reel(self, duration=30):
        time.sleep(duration)

    def next_reel(self):
        dd.swipe(1000, 300, 500, 300, self.index)
