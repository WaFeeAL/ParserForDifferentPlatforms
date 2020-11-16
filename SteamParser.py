# # def get_all_steam_games():
# #     r = requests.get('https://api.rawg.io/api/games')
# #     d = json.loads(r.content)
# #     response = d['applist']['apps']
# #
# #     with open(r"C:\Users\Herob\PycharmProjects\pythonProject\GamesList.json", "w") as write_file:
# #         json.dump(response, write_file)
#
# def get_all_steam_games():
#     r = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')
#     d = json.loads(r.content)
#     response = d['applist']['apps']
#
#     with open(r"C:\Users\Herob\PycharmProjects\pythonProject\GamesList.json", "w") as write_file:
#         json.dump(response, write_file)
#
#
# def get_info_about_game():
#     with open(r"C:\Users\Herob\PycharmProjects\pythonProject\GamesList.json", "r") as read_file:
#         game_data = json.load(read_file)
#     final_string = "["
#     for game in game_data:
#         link = f"https://store.steampowered.com/api/appdetails?appids={game['appid']}"
#         headers = {
#             "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 YaBrowser/20.4.2.150 (beta) Yowser/2.5 Safari/537.36'}
#         request = requests.get(link, headers)
#         data = json.loads(request.content)
#         if data[str(game['appid'])]['success']:
#             if data[str(game['appid'])]['data']['type'] == 'game':
#                 # print('{', end='')
#                 final_string += "{"
#                 for key, value in data[str(game['appid'])]['data'].items():
#                     if key == 'steam_appid' or key == 'name' or key == 'detailed_description' or key == 'required_age':
#                         if type(value) == str:
#                             # print(f'"{key}":"{value}"', end='')
#                             final_string += f'"{key}":"{value}"'
#                         else:
#                             # print(f'"{key}":{value}', end='')
#                             final_string += f'"{key}":{value}'
#
#                     if key == 'pc_requirements' and data[str(game['appid'])]['data']['platforms']['windows']:
#                         # print(f'"{key}":{value}', end='')
#                         final_string += f'"{key}":{value}'
#
#                     if key == 'mac_requirements' and data[str(game['appid'])]['data']['platforms']['mac']:
#                         # print(f'"{key}":{value}', end='')
#                         final_string += f'"{key}":{value}'
#
#                     if key == 'linux_requirements' and data[str(game['appid'])]['data']['platforms']['linux']:
#                         # print(f'"{key}":{value}', end='')
#                         final_string += f'"{key}":{value}'
#
#                     if key == 'release_date':
#                         # print(f'"{key}":{value}' + '},', end='')
#                         final_string += f'"{key}":{value}' + '},'
#                 # print(data[str(game['appid'])]['data'].items())
#     final_string += "]"
#
#     # print(final_string)
#     final_json = json.loads(final_string.content)
#     with open(r"C:\Users\Herob\PycharmProjects\pythonProject\FinalGameInfo.json", "w") as write_file:
#         json.dump(final_json, write_file)
#
#
# def temp():
#     with open(r"C:\Users\Herob\PycharmProjects\pythonProject\GamesList.json", "r") as read_file:
#         game_data = json.load(read_file)
#     # final_string = ""
#     # handle = open(r"C:\Users\Herob\PycharmProjects\pythonProject\FinalGameInfo.txt", "w")
#     for game in game_data:
#         link = f"https://store.steampowered.com/api/appdetails?appids={game['appid']}"
#         request = requests.get(link)
#         if request.status_code == requests.codes.ok:
#             data = json.loads(request.content)
#
#             if data is None:
#                 # handle.write(str(game['appid']) + ' is Null\n')
#                 print('Is Null')
#                 continue
#
#             if data[str(game['appid'])]['success']:
#                 # handle.write(str(game['appid']) + ' is OKEY!\n')
#                 print(str(game['appid']))
#             time.sleep(15)
#         else:
#             print(request.raise_for_status())
#     # handle.close()
#