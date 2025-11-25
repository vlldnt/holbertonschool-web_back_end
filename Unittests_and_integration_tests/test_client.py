#!/usr/bin/env python3
'''
Docstring pour Unittests_and_integration_tests.test_client
'''

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    def test_public_repos_url(self):
        """_public_repos_url uses repos_url from mocked org property"""
        payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
            }
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock,
                          return_value=payload):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """public_repos returns repo names; get_json and _public_repos_url used once"""
        repos_payload = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = repos_payload

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/testorg/repos",
        ) as mock_url:
            client = GithubOrgClient("testorg")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/testorg/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """has_license matches expected boolean for provided repo and license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
    for (org_payload, repos_payload, expected_repos, apache2_repos) in TEST_PAYLOAD
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos using fixtures"""

    @classmethod
    def setUpClass(cls):
        """Patch requests.get so external calls are not made"""
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        def _response(payload):
            class MockResp:
                def __init__(self, data):
                    self._data = data

                def json(self):
                    return self._data

            return MockResp(payload)

        def side_effect(url):
            if url == GithubOrgClient.ORG_URL.format(org="google"):
                return _response(cls.org_payload)
            if url == cls.org_payload.get("repos_url"):
                return _response(cls.repos_payload)
            return _response(None)

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """public_repos returns expected repo names from fixtures"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """public_repos filters by license 'apache-2.0' as expected"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)