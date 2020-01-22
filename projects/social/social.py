import random
personal_names = '''
James
John
Robert
Michael
William
David
Richard
Joseph
Thomas
Charles
Christopher
Daniel
Matthew
Anthony
Donald
Mark
Paul
Steven
Andrew
Kenneth
Joshua
George
Kevin
Brian
Edward
Ronald
Timothy
Jason
Jeffrey
Ryan
Jacob
Gary
Nicholas
Eric
Stephen
Jonathan
Larry
Justin
Scott
Brandon
Frank
Benjamin
Gregory
Samuel
Raymond
Patrick
Alexander
Jack
Dennis
Jerry
Mary
Patricia
Jennifer
Linda
Elizabeth
Barbara
Susan
Jessica
Sarah
Karen
Nancy
Margaret
Lisa
Betty
Dorothy
Sandra
Ashley
Kimberly
Donna
Emily
Michelle
Carol
Amanda
Melissa
Deborah
Stephanie
Rebecca
Laura
Sharon
Cynthia
Kathleen
Helen
Amy
Shirley
Angela
Anna
Brenda
Pamela
Nicole
Ruth
Katherine
Samantha
Christine
Emma
Catherine
Debra
Virginia
Rachel
Carolyn
Janet
'''.strip().split('\n')

surnames = '''
Sallow
Fernsby
Villin
Miracle
Dankworth
Relish
MacQuoid
Loughty
Birdwhistle
Berrycloth
Culpepper
Tumbler
Ajax
Edevane
Gastrell
Slora
Bread
MacCaa
Spinster
Pussett
Bythesea
Gotobed
'''

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for n in range(num_users):
            self.add_user(
                random.choice(personal_names) + ' ' + random.choice(surnames))

        # Create friendships
        for n in range(avg_friendships * num_users // 2):
            found_new = False
            maybe_as = random.shuffle(range(self.last_id + 1))
            for maybe_a in maybe_as:
                maybe_bs = random.shuffle(range(self.last_id + 1))
                for maybe_b in maybe_bs:
                    if maybe_b not in self.friendships[maybe_a]
                            and maybe_a != maybe_b:
                        self.add_friendship(maybe_a, maybe_b)
                        found_new = True
                        break
                if found_new:
                    break

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
