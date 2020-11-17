import threading
import RawgParser

# import SteamParser not available yet

if __name__ == '__main__':
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
    rawg_key = ''

    # Loop for RAWG
    for index in range(amount_of_threads):
        thread = threading.Thread(target=RawgParser.get_rawg, args=(start_page_number, file_number, STEP, rawg_key))
        thread.start()
        # Each next thread should deal with its own area
        start_page_number += STEP
        # Increasing the file number
        file_number += 1
