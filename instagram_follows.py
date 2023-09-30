from typing import Set

def read_follow_file(path: str) -> Set[str]:
    usernames = set()
    with open(path, "r") as file:
        for line in file:
            if "profile picture" in line:
                usernames.add(line.split("'")[0])
    return usernames

if __name__ == "__main__":
    followers_set = read_follow_file("followers.txt")
    following_set = read_follow_file("following.txt")

    print(f"{len(followers_set)}\t{len(following_set)}")

    followers_i_dont_follow_back = followers_set - following_set
    following_they_dont_follow_me = following_set - followers_set

    print(f"I don't follow back: {followers_i_dont_follow_back}\n")
    print(f"They don't follow back: {following_they_dont_follow_me}\n")
