from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting
from urllib.parse import urljoin


class GoogleCloudMediaFileStorage(GoogleCloudStorage):

    def url(self, name):  # Accept only one positional argument
        return urljoin(settings.MEDIA_URL, name)
