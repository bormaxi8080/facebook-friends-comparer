# -*- coding: utf-8 -*-

import os
import datetime
import json


def get_diff(friends1, friends2):
    diff = []
    for friend1 in friends1:
        exists = False
        for friend2 in friends2:
            if friend2["name"] == friend1["name"]:
                exists = True
                break
        if not exists:
            diff.append(friend1)
    return diff


class FacebookFiendListsComparer(object):
    def __init__(self, old_friends, new_friends):
        self.old_friends = old_friends
        self.new_friends = new_friends

    def compare(self):
        deleted_friends = get_diff(self.old_friends, self.new_friends)
        new_friends = get_diff(self.new_friends, self.old_friends)
        return {
            "deleted_friends": deleted_friends,
            "new_friends": new_friends
        }


def main():
    print("Start compare friends lists...")
    print("")

    old_list_path = "./data/old_friends.json"
    new_list_path = "./data/new_friends.json"

    if os.path.exists(old_list_path):
        with open(old_list_path, "r") as f:
            loaded_json = json.load(f)
            old_friends = loaded_json["friends_v2"]
    else:
        raise Exception("File does not exist: {0}".format(old_list_path))

    if os.path.exists(new_list_path):
        with open(new_list_path, "r") as f:
            loaded_json = json.load(f)
            new_friends = loaded_json["friends_v2"]
    else:
        raise Exception("File does not exist: {0}".format(old_list_path))

    comparer = FacebookFiendListsComparer(old_friends, new_friends)
    diff_json = comparer.compare()

    with open("./data/diff.json", "w") as f:
        json.dump(diff_json, f, indent=4)

    print("Deleted friends:")
    print("")
    for item in diff_json["deleted_friends"]:
        name = item["name"].encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8')
        print(name)
    print("")
    print("New friends:")
    print("")
    for item in diff_json["new_friends"]:
        name = item["name"].encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8')
        print(name)

    print("")
    print("Finish compare friends")


if __name__ == "__main__":
    main()
