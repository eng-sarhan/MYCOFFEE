from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# from django.utils.translation import ugettext_lazy as _
# import datetime
# from django_countries.fields import CountryField
# from django.utils.text import slugify
# from django.urls import reverse
# from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product_favorites=models.ManyToManyField(Product)
    #     slug = models.SlugField(blank=True, null=True)
    #     image = models.ImageField(_("image"), upload_to='profile_img', blank=True, null=True)
    #     country = CountryField()
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)

    #     join_date = models.DateTimeField(_("join date"), default=datetime.datetime.now)
    #
    #     def save(self, *args, **kwargs):
    #         if not self.slug:
    #             self.slug = slugify(self.user.username)
    #         super(Profile, self).save(*args, **kwargs)
    #
    #     class Meta:
    #         verbose_name = _("Profile")
    #         verbose_name_plural = _("Profiles")
    #
    def __str__(self):
        return '%s' % (self.user)

#     def get_absolute_url(self):
#         return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})
#
#
# def create_profile(sender, **kwargs):
#     print(kwargs)
#     if kwargs['created']:
#         user_profile = Profile.objects.create(user=kwargs['instance'])
#
#
# post_save.connect(create_profile, sender=User)