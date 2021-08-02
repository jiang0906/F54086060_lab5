import pygame
import os

UPGRADE_MENU = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_BTN = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_BTN = pygame.image.load(os.path.join("images", "sell.png"))

class UpgradeMenu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__buttons = [Button(UPGRADE_BTN, "upgrade", self.x - 35, self.y - 115),
                          Button(SELL_BTN, "sell", self.x - 25, self.y + 70)]  # (Q2) Add buttons here
        self.menu = pygame.transform.scale(UPGRADE_MENU, (250, 250))
        self.upgrade = pygame.transform.scale(UPGRADE_BTN, (70, 50))
        self.sell = pygame.transform.scale(SELL_BTN, (50, 50))
        pass


    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu, (self.x - self.menu.get_width() / 2, self.y - 125))
        # draw button
        win.blit(self.upgrade, (self.x - 35, self.y - 115))
        win.blit(self.sell, (self.x - 25, self.y + 70))


    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons
        pass


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        if self.x <= x <= self.x + self.width:
            if self.y <= y <= self.y + self.height:
                return True
        return False
        pass


    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name
        pass