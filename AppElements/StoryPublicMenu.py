import time

import droid_do as dd

from Utils.Point import Point


class StoryPublicMenu(object):
    def __init__(self, index):
        self.index = index
        self.public_story = Point(171, 1227)

    def click_public_story(self):
        dd.click_point(self.public_story, self.index)
        time.sleep(1)
