


class BrassBirmingham:


    def __init__(self):


        self.player_count =

        self.players =

        self.deck =



    def play_game(self):

        for era in ['canal', 'rail']: #canal era and rail era

            self.deck.reset()

            for player in self.players:
                player.hand = self.deck.deal(8)

            while self.deck.unplayed:

                for player in game.player_order:

                    player_action =


    def build(self, tile, location):
        """ """
        if tile.industry in location.available_industries:

            if tile.coal_cost:
                if location.has_coal:

            if tile.iron_cost:

            if tile.
            location.add_tile(tile)

    def place_link(self, player, A, B):





class Player:

    def __init__(self):

        self.hand

        self.inventory = [] #list of class objects of type Tile which they have in their stack maybe dict??

        self.money

        self.network = #node x structure


    def find_possible_actions(self):


class
























































