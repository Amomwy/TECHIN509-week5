import pandas as pd


class Log:
    def __init__(self, game):
        self.game = game
        self.log_file_path = "./data/log.csv"

    def log(self):
        _players = self.game.get_players()

        last_game_data_df = pd.read_csv(self.log_file_path)

        this_game_data_dict = {
            "game_id": [str(self.game.get_game_id())],
            "x_username": [_players[0].get_username()],
            "o_username": [_players[1].get_username()],
            "game_result": [self.game.get_winner()],
        }

        this_game_data_df = pd.DataFrame.from_dict(this_game_data_dict)

        new_game_data_df = pd.concat([last_game_data_df, this_game_data_df])

        new_game_data_df.to_csv(self.log_file_path, index=False)
