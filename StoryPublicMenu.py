import time

import droid_do as dd


class StoryPublicMenu(object):
    def __init__(self, index):
        self.index = index
        self.x_public_story = 171
        self.y_public_story = 1227

    def click_public_story(self):
        dd.click(self.x_public_story, self.y_public_story, self.index)
        time.sleep(1)
