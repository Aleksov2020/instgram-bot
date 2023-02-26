import time

import droid_do as dd
from Point import Point

class AccountPage(object):
    """
        Account page. Starts with posts
    """
    def __init__(self, index):
        self.index = index
        self.stories = Point(91, 195)
        self.pinned_stories = Point(71, 635)
        self.posts = Point(117, 769)
        self.reels = Point(360, 711)
        self.subscribe = Point(161, 517)

    def click_stories(self):
        dd.click_point(self.stories, self.index)
        time.sleep(1)

    def click_pinned_stories(self):
        dd.click_point(self.pinned_stories, self.index)
        time.sleep(1)

    def click_posts(self):
        dd.click_point(self.posts, self.index)
        time.sleep(1)

    def click_reels(self):
        dd.click_point(self.reels, self.index)
        time.sleep(1)

    def click_subscribe(self):
        dd.click_point(self.subscribe, self.index)
        time.sleep(1)

    def select_reel(self, reel_index=0):
        if 0 <= reel_index <= 2:
            dd.click(150 + reel_index * 200, 1000, self.index)
        elif 3 <= reel_index <= 5:
            dd.swipe(350, 1000, 350, 400, self.index)
            dd.click(150 + (reel_index - 3) * 200, 900, self.index)
    # TODO click on reel

