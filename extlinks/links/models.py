from django.db import models

from extlinks.programs.models import Collection


class URLPattern(models.Model):
    class Meta:
        app_label = "links"
        verbose_name = "URL pattern"
        verbose_name_plural = "URL patterns"

    # This doesn't have to look like a 'real' URL so we'll use a CharField.
    url = models.CharField(max_length=60)

    collection = models.ForeignKey(Collection, null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return self.url


class LinkSearchTotal(models.Model):
    class Meta:
        app_label = "links"
        verbose_name = "LinkSearch total"
        verbose_name_plural = "LinkSearch totals"

    url = models.ForeignKey(URLPattern, null=True,
                            on_delete=models.SET_NULL)

    date = models.DateField(auto_now_add=True)
    total = models.PositiveIntegerField()


class LinkEvent(models.Model):
    """
    Stores data from the page-links-change EventStream

    https://stream.wikimedia.org/?doc#!/Streams/get_v2_stream_page_links_change
    """
    class Meta:
        app_label = "links"

    url = models.ForeignKey(URLPattern, null=True,
                            on_delete=models.SET_NULL)

    # URLs should have a max length of 2083
    link = models.CharField(max_length=2083)
    timestamp = models.DateTimeField()
    domain = models.CharField(max_length=32)
    username = models.CharField(max_length=255)
    rev_id = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    page_title = models.CharField(max_length=255)
    page_namespace = models.IntegerField()

    # Were links added or removed?
    REMOVED = 0
    ADDED = 1

    CHANGE_CHOICES = (
        (REMOVED, 'Removed'),
        (ADDED, 'Added'),
    )

    change = models.IntegerField(choices=CHANGE_CHOICES)

    # Flags whether this event was from a user on the user list for the
    # organisation tracking its URL.
    on_user_list = models.BooleanField(default=False)