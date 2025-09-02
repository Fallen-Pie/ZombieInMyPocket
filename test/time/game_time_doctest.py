"""
>>> from src.model.game_time.game_time import GameTime
>>> game_time = GameTime()


>>> game_time.get_current_time()
9

>>> game_time._is_am()
False

>>> game_time._get_am_pm()
'PM'

>>> game_time.is_time_valid()
True

>>> str(game_time)
'The time is now 09:00PM'

>>> game_time.increase_time()

>>> game_time.get_current_time()
10

>>> game_time._is_am()
False

>>> game_time._get_am_pm()
'PM'

>>> game_time.is_time_valid()
True

>>> str(game_time)
'The time is now 10:00PM'

>>> game_time.increase_time()

>>> str(game_time)
'The time is now 11:00PM'

>>> game_time.increase_time()

>>> game_time.is_time_valid()
False

>>> game_time._is_am()
True

>>> game_time._get_am_pm()
'AM'
"""

def test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == '__main__':
    test()