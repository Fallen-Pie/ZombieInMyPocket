import unittest
from unittest.mock import Mock

class TestAlertMessageManager(unittest.TestCase):
    def setUp(self):
        """ Mocking dependencies"""
        pass

    def test_low_health_warning_message(self):
        """
        🟡 Scenario (Alternate Flow) Display Low Health Warning
        •	Given an “Event” occurred
        •	When the player’s health stat decreased to 1*
        •	Then display warning message 'Warning! Your health is running low '
        """
        pass

    def test_near_midnight_warning_message(self):
        """
        🟡 Scenario (Alternate Flow) Display Time Warning
        •	Given a player action is performed (acquiring items, drawing a card, or changing room)
        •	When the time reaches 11PM
        •	Then display warning message 'Hurry! Your time is running out!'
        """
        pass

    def test_zombie_door_created(self):
        """
        🟡 Scenario (Alternate Flow) Display Zombie Doors created when exits are none
        •	Given the player has made a minimum of 1 move since the start of the game
        •	When the player enters a new room tile that only has one exit (i.e. Bathroom or Storage)
        •	And the user gets prompted to choose which side of the room to create a zombie door
        •	Then display the informational message: “No more exits. Zombie door is created on [Chosen direction]. Three (3) zombies incoming.”
        """
        pass

if __name__ == '__main__':
    unittest.main()