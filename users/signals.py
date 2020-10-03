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
        user = instance.user.username
        playlist = Playlist.objects.get(pk=pk_set.pop())
        playlist_author = playlist.user
        try:
            send_mail(
            subject="Someone added your playlist to favorites",
            message="""
            Hi, {playlist_author}! {user} added your playlist {playlist} to their favorites. You're making quite a name for yourself in the music scene. Cheers!
            """.format(playlist_author=playlist_author.username, user=user, playlist=playlist),
            from_email=None,
            recipient_list=[playlist_author.email]
            )
        except:
            print("error: maybe email not found?")