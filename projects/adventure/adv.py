from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from collections import deque

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
'''
tree = {}

def add_node(node_id):
    tree[node_id] = {}

def add_edge(from_n, to_n, direction):
    tree[from_n][direction] = to_n
    tree[to_n]['anti' + direction] = from_n # not sure backtracking needed
'''

def df_recursive(room):
    visited = set()
    path = []

    def df_recur(room, from_direction=None):
        visited.add(room.id)
        for direction in room.get_exits():
            next_room = room.get_room_in_direction(direction)
            if next_room.id in visited:
                continue
            visited.add(next_room.id)
            path.append(direction)
            df_recur(
                room.get_room_in_direction(direction),
                from_direction=direction)
        if from_direction is not None:
            other_way = {
                'n': 's',
                's': 'n',
                'e': 'w',
                'w': 'e',
            }[from_direction]
            path.append(other_way)

    df_recur(room)
    return path

traversal_path = df_recursive(world.starting_room)
print(traversal_path)
'''
queue = deque()
queue.append(player.current_room)
visited = set()
while len(queue) > 0:
    room = queue.popleft()
    if room not in visited:
        add_node(room.id)
        add_edge(previous_id, room.id, some_direction)
        visited.add(room.id)
        for next_vertex in self.get_neighbors(vertex):
            new_path = path + [next_vertex]
            queue.enqueue(new_path)
'''

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
