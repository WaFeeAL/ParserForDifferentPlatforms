import json
import time
import requests

# Last RAWG game page (13.11.2020). Determined manually
LAST_RAWG_GAME_PAGE = 23318


def get_rawg(start_page_number, file_number, STEP, rawg_key):
    # Every request to RAWG API should have user-agent header with app name.
    # If we don't provide it, his may be ban our requests.(Ctrl + Shift + I, Network tab, Reload page, Pick longer line)
    header = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 " \
             "YaBrowser/20.4.2.150 (beta) Yowser/2.5 Safari/537.36"

    # Because sometimes us need to parse a lot of information, we created some threads and give them start page
    # number from which will start parsing, and also give them file number, which we will write information.
    # 'index' will be used like iterator reflecting the current page.
    index = start_page_number

    # Create or re-create file and write '[' to maintain .json format.
    f = open(rf"C:\Users\Herob\PycharmProjects\ParserForDifferentPlatforms\rawg_game_data\rawg_game_data_{file_number}.txt", "w",
             encoding="utf8")
    f.write('[')
    f.close()

    # Open the file for writing to the end.
    f = open(rf"C:\Users\Herob\PycharmProjects\ParserForDifferentPlatforms\rawg_game_data\rawg_game_data_{file_number}.txt", "a",
             encoding="utf8")

    # A loop that checks whether the required interval has passed, or the last page.
    while index != start_page_number + STEP and index != LAST_RAWG_GAME_PAGE + 1:
        link_to_page = f"https://api.rawg.io/api/games?key={rawg_key}&page={index}"

        # Making a request for a page. Here we just need header.
        page_data = requests.get(link_to_page, header)

        # If the connection fails the first time, wait 5 seconds and try again. And so until we connect. Since we
        # know that we haven't reached the end yet and the page definitely exists.
        while page_data.status_code != requests.codes.ok and page_data is None:
            time.sleep(5)
            page_data = requests.get(link_to_page, header)


        # game = json.loads(page_data.content)

        # We translate the received information into .json format and take the key we need.
        page_data = json.loads(page_data.content)['results']

        # Now we will extract one game from the values of the "results" key.
        for game in page_data:
            link_to_game = f"https://api.rawg.io/api/games/{game['id']}?key={rawg_key}"

            # The same procedure as with the page, only for the game.
            game_data = requests.get(link_to_game, header)

            while game_data.status_code != requests.codes.ok and game_data is None:
                time.sleep(5)
                game_data = requests.get(link_to_game, header)

            game_data = json.loads(game_data.content)

            # To maintain .json format. Open "{" and write down the information we need about the game.
            f.write('{')

            # We select the key we need, check its value for correctness and write it to a file.
            for key, value in game_data.items():
                if key == 'id' or key == 'name' or key == 'description':
                    if type(value) == str:
                        f.write(f'"{key}":"{value}",')
                    else:
                        f.write(f'"{key}":{value},')

                if key == 'released':
                    if value is not None and value:
                        f.write(f'"{key}":{value},')
                    else:
                        f.write(f'"{key}": None,')

                if key == 'platforms':
                    if value:
                        f.write(f'"requirements":{value[0]["requirements"]},')
                    else:
                        f.write(f'"requirements": None,')

                if key == 'esrb_rating':
                    if value is not None and value:
                        if type(value['name']) == str:
                            f.write(f'"{key}":"{value["name"]}"')
                    else:
                        f.write(f'"{key}": None')

            # When we have written down all the necessary information about the game, close "}".
            f.write('},\n')

        # Go to the next page.
        index += 1

    # Closes "]" to maintain .json format.
    f.write("]")

    # Close the file.
    f.close()
