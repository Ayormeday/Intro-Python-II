from room import Room
from player import Player
from items import Items

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

direction_list = ['N', 'S', 'E', 'W']
possible_direction = []
initial_room = 'outside'
new_player = Player(room[initial_room], [])

quit_game = False


def main():
    global direction_list, initial_room, new_player, quit_game

    while not quit_game:
        #player's initial location
        print(f"Player arrives at the {new_player.room.name} {new_player.room.description}\n")

        #directions player can move towards
        possible_direction = [key.split("_")[0].upper() for key, val in vars(new_player.room).items() if key not in ['name', 'description', 'key']]
        for direction in direction_list:
            if direction in possible_direction:
                print(f"[{direction}] is a possible route to take")
            else:
                print(f"Not a valid route!")

        #take player input
        player_input = input("Which direction would you like to move towards?\n")
        input_split = player_input.split(' ')
        input_direction = input_split[:1].upper()
        user_input = input_split[1:]

        #player move commandline
        if input_direction in ['GO', 'GOTO', 'ROOM', 'TRAVEL', 'T']:
            takeDirection(user_input[0].upper())
        elif input_direction in ['GET', 'PICK', 'PICKUP', 'LOOT', 'G', 'P', 'L']:
            inputItem = ''.join(user_input[1:]).lower().capitalize()
            inputItem = [item for item in items if item.name == inputItem]
            inputQty = int(user_input[:1][0])
            if len(inputItem) > 0:
                new_player.getItem(inputItem[0], inputQty)
            else:
                print('item does not exist!')
        elif input_direction in ['DROP', 'REM', 'REMOVE', 'DESTROY', 'D', 'R']:
            inputItem = ''.join(user_input[1:]).lower().capitalize()
            inputItem = [item for item in items if item.name == inputItem]
            inputQty = int(user_input[:1][0])
            if len(inputItem) > 0:
                new_player.dropItem(inputItem[0], inputQty)
            else:
                print('item does not exist!')
        elif input_direction in ['I', 'INV', 'INVENTORY', 'ITEMS']:
            if len(new_player.inventory) > 0:
                print('\nHere\'s what you have:')
                for item in new_player.inventory:
                    print(f'{item.qty}x [{item.name}] - {item.description}')
            else:
                print('\nThere is nothing in your inventory!')
        elif input_direction in ['Q', 'QUIT', 'EXIT', 'STOP']:
            print("Giving up already? Weak adventurers shouldn't even have started!")
            quitGame = True
        else:
            print('Invalid command.')

        print('\n')

        #items visible to players in the room
        print(f"These items are visible in {new_player.room.name} room")
        for item in new_player.room.items:
           print(f"\n {item.name}\n {item.description}")


        def takeDirection(direction):
            global direction_list, new_player, quit_game
            if direction == 'N' and direction in possible_direction:
                new_player.openRoom(new_player.room.n_to)
            elif direction == 'E' and direction in possible_direction:
                new_player.openRoom(new_player.room.e_to)
            elif direction == 'S' and direction in possible_direction:
                new_player.openRoom(new_player.room.s_to)
            elif direction == 'W' and direction in possible_direction:
                new_player.openRoom(new_player.room.w_to)
            elif direction in direction_list and direction not in possible_direction:
                print("Congrats! Count the bricks on the wall!")
            elif direction not in direction_list:
                print("Try N, E, S or W!")
          

