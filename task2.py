import requests
from collections import Counter
from geopy.distance import geodesic
from copy import deepcopy


def build_users_dict(users_list, key):
    """Build users dict by key from a list."""
    return dict([(user.pop(key), user) for user in users_list])


def read_json_from_url(url):
    """Read json from url and return its content."""
    response = requests.get(url)
    json_content = response.json()
    return json_content


def count_posts_per_user(posts, user_ids):
    """Count posts written by every user. Return a dict mapping user ids to post counts."""
    count = dict([(user_id, 0) for user_id in user_ids])
    for post in posts:
        count[post["userId"]] += 1
    return count


def select_non_uniq_strings(titles):
    """Take a list of strings and return a list of non unique titles."""
    title_count = Counter(titles)
    # title_count = Counter([post["title"] for post in posts])
    non_uniq_titles = [title for (title, count) in title_count.items() if count > 1]
    return non_uniq_titles


def find_nearest(id, users_loc):
    """Take a user id as an input and dictionary of users and their
    geo-locations (as tuples). Return id of other user located nearest to them.
    """
    curr_loc = users_loc.pop(id)
    min_distance = 10e8  # initialze with some value bigger than possible on Earth

    for user_id, loc in users_loc.items():
        distance = geodesic(curr_loc, loc).kilometers
        if distance < min_distance:
            min_distance = distance
            nearest_user = user_id

    return nearest_user


def main():
    posts_url = "https://jsonplaceholder.typicode.com/posts"
    users_url = "https://jsonplaceholder.typicode.com/users"

    posts = read_json_from_url(posts_url)
    users = read_json_from_url(users_url)

    # Connect posts data and users data
    users_dict = build_users_dict(deepcopy(users), "id")
    posts_users = [(post, users_dict[post["userId"]]) for post in posts]

    # Count posts written by each user
    user_ids = [id for id in users_dict.keys()]
    users_names = dict([(user["id"], user["name"]) for user in users])
    user_count = count_posts_per_user(posts, users_names)
    name_count = ["User {0} wrote {1} posts.".format(users_names[user_id], user_count[user_id])
                  for user_id in users_names.keys()]
    print(name_count)

    # Find non unique post titles
    non_uniq_titles = select_non_uniq_strings([post["title"] for post in posts])
    print("List of non unique titles:", non_uniq_titles)

    # For each user find another user located nearest to them
    users_locations = dict([(user["id"], tuple(user["address"]["geo"].values())) for user in users])
    nearest_users = {}
    for user in users:
        nearest_users[user["id"]] = find_nearest(user["id"], users_locations.copy())

    # Output in a manner: {user_id: nearest_users'_id}
    print(nearest_users)

if __name__ == "__main__":
    main()
