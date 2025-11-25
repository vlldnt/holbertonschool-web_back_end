#!/usr/bin/env python3
'''
Docstring pour Unittests_and_integration_tests.test_client
'''

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """org returns mocked payload; get_json called once with expected URL"""
        fake_payload = {"login": org_name, "id": 1,
                        "repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        mock_get_json.return_value = fake_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, fake_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
