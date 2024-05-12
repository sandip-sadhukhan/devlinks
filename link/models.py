from django.db import models

class PlatformLink(models.Model):
    GITHUB = 1
    TWITTER = 2
    LINKEDIN = 3
    YOUTUBE = 4
    FACEBOOK = 5
    TWITCH = 6
    DEV_TO = 7
    CODE_WARS = 8
    CODE_PEN = 9
    FREE_CODE_CAMP = 10
    GITLAB = 11
    HASH_NODE = 12
    STACK_OVERFLOW = 13

    PLATFORM_CHOICES = (
        (GITHUB, "GitHub"),
        (TWITTER, "Twitter"),
        (LINKEDIN, "LinkedIn"),
        (YOUTUBE, "Youtube"),
        (FACEBOOK, "Facebook"),
        (TWITCH, "Twitch"),
        (DEV_TO, "Dev.to"),
        (CODE_WARS, "Codewars"),
        (CODE_PEN, "Codepen"),
        (FREE_CODE_CAMP, "FreeCodeCamp"),
        (GITLAB, "GitLab"),
        (HASH_NODE, "Hashnode"),
        (STACK_OVERFLOW, "Stack Overflow"),
    )

    platform = models.IntegerField(choices=PLATFORM_CHOICES)
    link_address = models.URLField()
    position = models.IntegerField(help_text="Position of the link in the list,"
                                   "start with 1", default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey("accounts.User", on_delete=models.CASCADE,
                                   related_name="platform_links")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.platform} - {self.link_address}"
