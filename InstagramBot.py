import random
import time
import droid_do as dd

from AppElements.AccountPage import AccountPage
from AppElements.BottomMenu import BottomMenu
from AppElements.Reel import Reel
from AppElements.SearchPage import SearchPage
from AppElements.SendMenu import SendMenu
from AppElements.StoryPublicMenu import StoryPublicMenu


class InstagramBot(object):
    def __init__(self, index):
        self.index = index
        self.account_page = AccountPage(index)
        self.bottom_menu = BottomMenu(index)
        self.reel = Reel(index)
        self.search_page = SearchPage(index)
        self.send_menu = SendMenu(index)
        self.story_public_menu = StoryPublicMenu(index)
        print("Open insta")
        self.open_instagram()

    def watch_target_reel(self, account_name):
        self.bottom_menu.click_search()
        self.search_page.click_search_field()
        dd.input_text(self.index, account_name)
        self.search_page.click_first_result()
        self.account_page.click_reels()
        self.account_page.select_reel(0)
        time.sleep(5)
        self.reel.watch_reel()
        self.reel.click_like_button()
        # SAVE
        time.sleep(15)
        # SAVE END


        time.sleep(2)
        self.reel.click_send_button()
        time.sleep(2)
        self.send_menu.click_send_reel_to_story()
        time.sleep(2)
        self.story_public_menu.click_public_story()
        time.sleep(2)
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
