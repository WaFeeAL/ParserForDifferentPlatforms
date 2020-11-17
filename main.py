import threading
import modules.rawg.RawgParser as RawgParser
import modules.rawg.rawg_developers_parser as rawg_get_developers


# import SteamParser not available yet

def rawg_game_parser():
    # Number of file which we will create
    file_number = 1

    # FOR RAWG PARSER
    # It means how much pages will be parsed by 1 thread
    STEP = 500
    # Page which will start parsing for 1 thread
    start_page_number = 1
    # Amount of threads :D
    amount_of_threads = 47
    # Your RAWG key
    rawg_key = '21de55e5fa7f42e28f7c5696e7b110e0'

    # Loop for RAWG
    for index in range(amount_of_threads):
        thread = threading.Thread(target=RawgParser.get_rawg, args=(start_page_number, file_number, STEP, rawg_key))
        thread.start()
        # Each next thread should deal with its own area
        start_page_number += STEP
        # Increasing the file number
        file_number += 1


def rawg_developers_parser():
    # Number of file which we will create
    file_number = 1

    # FOR RAWG PARSER
    # It means how much pages will be parsed by 1 thread
    STEP = 500
    # Page which will start parsing for 1 thread
    start_page_number = 1
    # Amount of threads :D
    amount_of_threads = 44
    # Your RAWG key
    rawg_key = '21de55e5fa7f42e28f7c5696e7b110e0'

    # Loop for RAWG
    for index in range(amount_of_threads):
        thread = threading.Thread(target=rawg_get_developers.get_rawg_developers, args=(start_page_number, file_number, STEP, rawg_key))
        thread.start()
        # Each next thread should deal with its own area
        start_page_number += STEP
        # Increasing the file number
        file_number += 1


if __name__ == '__main__':
    # rawg_game_parser()
    rawg_developers_parser()