from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Profile
from playlists.models import Playlist

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save

@receiver(m2m_changed, sender = Profile.favorites.through)
def send_email_after_favorite(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        send_mail(
            subject="Someone added your playlist to favorites",
            message="""
            Hi, {user}! Someone added your playlist {playlist} to their favorites. You're making quite a name for yourself in the music scene. Cheers!
            """.format(user=instance, playlist=Playlist.objects.get(pk=pk_set.pop())),
            from_email=None,
            recipient_list=["playitt.app@gmail.com"]
        )