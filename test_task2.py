from unittest import TestCase


class TestTask2(TestCase):
    def test_build_users_dict(self):
        """Test build_users_dict."""
        from task2 import build_users_dict
        data = [{"name": "Tom", "id": 101, "age": 15}, {"id": 55, "age": 30, "name": "Eva"}]
        key = "id"
        expect = {101: {"name": "Tom", "age": 15}, 55: {"age": 30, "name": "Eva"}}
        self.assertEqual(build_users_dict(data, key), expect)

    def test_count_posts_per_user(self):
        """Test count_posts_per_user."""
        from task2 import count_posts_per_user
        posts = [{"userId": 101, "id": 1, "title": "title one"},
                 {"userId": 42, "id": 2, "title": "title two"},
                 {"userId": 101, "id": 3, "title": "title three"}]
        ids = [42, 101]
        expect = {101: 2, 42: 1}
        self.assertEqual(count_posts_per_user(posts, ids), expect)

    def test_select_non_uniq_strings(self):
        """Test select non_uniq titles."""
        from task2 import select_non_uniq_strings
        titles = ["titleA", "titleB", "titleB", "titleC", "titleB", "titleC"]
        expect = ["titleB", "titleC"]
        self.assertCountEqual(select_non_uniq_strings(titles), expect)

    def test_find_nearest(self):
        """Test find_nearest"""
        from task2 import find_nearest
        data = {1: ('-10.5', '-10.5'), 2: ('88.9509', '134.4618'),
                3: ('-28.02', '0'), 4: ('76.4572', '164.2990')}
        id = 3
        expect = 1
        self.assertEqual(find_nearest(id, data), expect)
