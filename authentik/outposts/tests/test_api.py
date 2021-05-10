"""Test outpost service connection API"""
from django.urls import reverse
from rest_framework.test import APITestCase

from authentik.core.models import PropertyMapping, User
from authentik.flows.models import Flow
from authentik.outposts.api.outposts import OutpostSerializer
from authentik.outposts.models import default_outpost_config
from authentik.providers.proxy.models import ProxyProvider


class TestOutpostServiceConnectionsAPI(APITestCase):
    """Test outpost service connection API"""

    def setUp(self) -> None:
        super().setUp()
        self.mapping = PropertyMapping.objects.create(
            name="dummy", expression="""return {'foo': 'bar'}"""
        )
        self.user = User.objects.get(username="akadmin")
        self.client.force_login(self.user)

    def test_types(self):
        """Test OutpostServiceConnections's types endpoint"""
        response = self.client.get(
            reverse("authentik_api:outpostserviceconnection-types"),
        )
        self.assertEqual(response.status_code, 200)

    def test_outpost_config(self):
        """Test Outpost's config field"""
        provider = ProxyProvider.objects.create(name="test", authorization_flow=Flow.objects.first())
        invalid = OutpostSerializer(data={
            "name": "foo",
            "providers": [provider.pk],
            "config": {}
        })
        self.assertFalse(invalid.is_valid())
        self.assertIn("config", invalid.errors)
        valid = OutpostSerializer(data={
            "name": "foo",
            "providers": [provider.pk],
            "config": default_outpost_config("foo")
        })
        self.assertTrue(valid.is_valid())
