import pytest
import os
from utils.browser_setup import get_driver
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_search_page import TwitchSearchPage
from pages.twitch_category_page import TwitchCategoryPage
from pages.twitch_streamer_page import TwitchStreamerPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_search_twitch_streamer(driver):
    home_page = TwitchHomePage(driver)
    search_page = TwitchSearchPage(driver)
    category_page = TwitchCategoryPage(driver)
    streamer_page = TwitchStreamerPage(driver)

    # Step 1
    home_page.navigate(os.getenv("TWITCH_URL"))
    # Step 2
    home_page.click_search_icon()
    # Step 3
    search_page.search_game_and_select("StarCraft II")
    # Step 4
    category_page.assert_streamers_are_visible()
    driver.execute_script("window.scrollBy(0, 20);")
    driver.execute_script("window.scrollBy(0, 20);")
    # Step 5
    category_page.select_random_streamer_on_page()
    # Step 6
    streamer_page.close_warning_popup_if_exist()
    streamer_page.wait_for_video_to_load()
    streamer_page.take_screenshot("streamer_page.png")
