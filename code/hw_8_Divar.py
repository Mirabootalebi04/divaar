
class User: 
    def __init__(self, username): 
        self.username = username 
        self.adverties = [] # List of posted ads
        self.favorites = [] # List of favorite ads

    def post_ad(self, title):
        self.adverties.append(title)

    def remove_ad(self, title):
        if title in self.adverties:
            self.adverties.remove(title)

    def add_favorite(self, title):
        if title not in self.favorites:
            self.favorites.append(title)

    def remove_favorite(self, title):
        if title in self.favorites:
            self.favorites.remove(title)  

class AdvertisementSystem: 
    def __init__(self): 
        self.user2object = {} # usernames to User objects 
        self.adtitle2usernsme = {}  # ad titles to usernames

    def register(self, username) :
        """
        used in cmd
        """
        if username in self.user2object :
            print("invalid username")
        else:
            self.user2object[username] = User(username)
            print("registered successfully")

    def add_advertise(self, username, title) :
        if username not in self.user2object:
            print("invalid username")
            return

        if title in self.adtitle2usernsme:
            print("invalid title")
            return

        f'# {self.user2object[username].post_ad(title)}'
        self.adtitle2usernsme[title] = username
        print("posted successfully")

    def rem_advertise(self, username, title):
        if username not in self.user2object:
            print("invalid username")
            return

        if title not in self.adtitle2usernsme:
            print("invalid title")
            return

        if self.adtitle2usernsme[title] != username:
            print("access denied")
            return

        self.user2object[username].remove_ad(title)
        del self.adtitle2usernsme[title]

        for user in self.user2object.values():
            user.remove_favorite(title)

        print("removed successfully")

    def list_my_advertises(self, username):
        if username not in self.user2object:
            print("invalid username")
            return

        print(" ".join(self.user2object[username].ads))

    def add_favorite(self, username, title):
        if username not in self.user2object:
            print("invalid username")
            return

        if title not in self.adtitle2usernsme:
            print("invalid title")
            return

        if title in self.user2object[username].favorites:
            print("already favorite")
            return

        self.user2object[username].add_favorite(title)
        print("added successfully")

    def rem_favorite(self, username, title):
        if username not in self.user2object:
            print("invalid username")
            return

        if title not in self.adtitle2usernsme:
            print("invalid title")
            return

        if title not in self.user2object[username].favorites:
            print("already not favorite")
            return

        self.user2object[username].remove_favorite(title)
        print("removed successfully")

    def list_favorite_advertises(self, username):
        if username not in self.user2object:
            print("invalid username")
            return

        print(" ".join(self.user2object[username].favorites))

#Input proces
if __name__ == "__main__":
    import sys
    system = AdvertisementSystem()

for line in sys.stdin:
    command = line.strip()
    if not command:
        continue

    parts = command.split()
    if not parts:
        continue

    cmd = parts[0]

    if cmd == "register" and len(parts) == 2:
        system.register(parts[1])

    elif cmd == "add_advertise" and len(parts) == 3:
        system.add_advertise(parts[1], parts[2])

    elif cmd == "rem_advertise" and len(parts) == 3:
        system.rem_advertise(parts[1], parts[2])
 
    elif cmd == "list_my_advertises" and len(parts) == 2:
        system.list_my_advertises(parts[1])

    elif cmd == "add_favorite" and len(parts) == 3:
        system.add_favorite(parts[1], parts[2])

    elif cmd == "rem_favorite" and len(parts) == 3:
        system.rem_favorite(parts[1], parts[2])

    elif cmd == "list_favorite_advertises" and len(parts) == 2:
        system.list_favorite_advertises(parts[1])
