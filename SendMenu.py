import time

import droid_do as dd


class SendMenu(object):
    def __init__(self, index):
        self.index = index
        self.x_search_field = 197
        self.y_search_field = 443
        self.x_send_reel_to_story = 225
        self.y_send_reel_to_story = 525
        self.x_add_text = 271
        self.y_add_text = 365
        self.x_first_result = 160
        self.y_first_result = 613
        self.x_send_message_first_result = 581
        self.y_send_message_first_result = 617

    def click_search_field(self):
        dd.click(self.x_search_field, self.y_search_field, self.index)
        time.sleep(1)

    def click_send_reel_to_story(self):
        dd.click(self.x_send_reel_to_story, self.y_send_reel_to_story, self.index)
        time.sleep(1)

    def click_add_text(self):
        dd.click(self.x_add_text, self.y_add_text, self.index)
        time.sleep(1)

    def click_first_result(self):
        dd.click(self.x_first_result, self.y_first_result, self.index)
        time.sleep(1)

    def click_first_result(self):
        dd.click(self.x_first_result, self.y_first_result, self.index)
        time.sleep(1)

    def click_send_message_first_result(self):
        dd.click(self.x_send_message_first_result, self.y_send_message_first_result, self.index)
        time.sleep(1)