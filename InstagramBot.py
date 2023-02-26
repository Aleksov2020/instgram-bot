import random
import time
import droid_do as dd

from AccountPage import AccountPage
from BottomMenu import BottomMenu
from Reel import Reel
from SearchPage import SearchPage
from SendMenu import SendMenu
from StoryPublicMenu import StoryPublicMenu


class InstagramBot(object):
    def __init__(self, index):
        self.index = index
        self.account_page = AccountPage(index)
        self.bottom_menu = BottomMenu(index)
        self.reel = Reel(index)
        self.search_page = SearchPage(index)
        self.send_menu = SendMenu(index)
        self.story_public_menu = StoryPublicMenu(index)
        self.open_instagram()

    def watch_target_reel(self, account_name):
        self.bottom_menu.click_search()
        self.search_page.click_search_field()
        dd.input_text(self.index, account_name)
        self.search_page.click_first_result()
        self.account_page.click_reels()
        self.account_page.select_reel(0)
        self.reel.watch_reel()
        self.reel.click_like_button()
        self.reel.click_send_button()
        self.send_menu.click_send_reel_to_story()
        self.story_public_menu.click_public_story()
        dd.back_button(self.index)
        dd.back_button(self.index)
        time.sleep(10)

    def watch_recommended_reels(self):
        probability_like = random.random()
        probability_repost = random.random()


        self.bottom_menu.click_reel()
        self.reel.watch_reel()

    def open_instagram(self):
        dd.click(361, 1021, self.index)
        time.sleep(5)