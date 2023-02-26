import time

import droid_do as dd


class AccountPage(object):
    """
        Account page. Starts with posts
    """
    def __init__(self, index):
        self.index = index
        self.x_stories = 91
        self.y_stories = 195
        self.x_pinned_stories = 71
        self.y_pinned_stories = 635
        self.x_posts = 117
        self.y_posts = 769
        self.x_reels = 360
        self.y_reels = 711
        self.x_subscribe = 161
        self.y_subscribe = 517

    def click_stories(self):
        dd.click(self.x_stories, self.y_stories, self.index)
        time.sleep(1)

    def click_pinned_stories(self):
        dd.click(self.x_pinned_stories, self.y_pinned_stories, self.index)
        time.sleep(1)

    def click_posts(self):
        dd.click(self.x_posts, self.y_posts, self.index)
        time.sleep(1)

    def click_reels(self):
        dd.click(self.x_reels, self.y_reels, self.index)
        time.sleep(1)

    def click_subscribe(self):
        dd.click(self.x_subscribe, self.y_subscribe, self.index)
        time.sleep(1)

    def select_reel(self, reel_index=0):
        if 0 <= reel_index <= 2:
            dd.click(150 + reel_index * 200, 1000, self.index)
        elif 3 <= reel_index <= 5:
            dd.swipe(350, 1000, 350, 400, self.index)
            dd.click(150 + (reel_index - 3) * 200, 900, self.index)
    # TODO click on reel

