from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
class Scroll_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def scroll_to_element_in_container(self, container_element, target_element):
        initial_scroll_position = container_element.get_property("scrollLeft")

        # Scroll the container horizontally until the target element is visible
        while target_element.text == None:
            # Perform a horizontal scroll action on the container
            actions = ActionChains(self.driver)
            actions.scroll_by_amount(600, 0).perform()
            # actions.drag_and_drop( container_element, target_element)
            

            # Check if we've scrolled too far
            current_scroll_position = container_element.get_property("scrollLeft")
            if current_scroll_position <= initial_scroll_position:
                break

            initial_scroll_position = current_scroll_position
    
    def double_click (self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        return BasePage()


