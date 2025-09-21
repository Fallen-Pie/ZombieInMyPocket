def test():
    from doctest import testfile
    test_file = (r"get_game_time_doctest.txt")

    testfile(f'{test_file}', verbose=True)

if __name__ == '__main__':
    test()