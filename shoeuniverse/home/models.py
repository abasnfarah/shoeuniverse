from __future__ import absolute_import, unicode_literals

from django.db import models
from django.shortcuts import render

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from wagtailgmaps.edit_handlers import MapFieldPanel

class HomePage(Page):
  body = RichTextField(blank=True)
  banner = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    ImageChooserPanel('banner'),
    InlinePanel('shoe_tiles', label="Shoe Types"),
  ]

class ShoeHistoryPage(Page):
  body = RichTextField(blank=True)
  shoeImage = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    ImageChooserPanel('shoeImage'),
    InlinePanel('style_tiles', label="Styles"),
  ]

class AboutPage(Page):
  body = RichTextField(blank=True)
  location = models.CharField(max_length=255)
  content_panels = Page.content_panels + [
    FieldPanel('body', classname='full'),
    MapFieldPanel('location'),
    InlinePanel('contributer', label="New Contrubuter"),
  ]

class Contributer(models.Model): 
  
  name = models.CharField(max_length=255, blank=True)
  role = models.CharField(max_length=255, blank=True)
  email = models.EmailField(max_length=255, default='youremail@swag.com')
  
  panel = [
    FieldPanel('name'),
    FieldPanel('role'),
    FieldPanel('email')    
  ] 
  
  class Meta:
    abstract = True
    verbose_name = 'Contributer'
    verbose_name_plural = 'Contributers'
  

class newContributer(Orderable, Contributer):
    page = ParentalKey(AboutPage, related_name='contributer')
    
class ShoeTile(models.Model):
  # Define objects within the tile (title, image, link)
  title = models.CharField(max_length=255, blank=True)
  image = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  

  # Define panel (similar to content_panel of a Page)
  panel = [
    FieldPanel('title'),  
  ]

  class Meta:
    abstract = True
    verbose_name = "Tile"
    verbose_name_plural = "Tiles"

class HomeShoeTile(Orderable, ShoeTile):
  embed_url = models.URLField("Embed URL", blank=True) 
  page = ParentalKey(HomePage, related_name='shoe_tiles')

  panel = [
    FieldPanel('embed_url'),
    FieldPanel('image'),
  ]

class StyleShoeTile(Orderable, ShoeTile):
  page = ParentalKey(ShoeHistoryPage, related_name='style_tiles')

  panel = [
    FieldPanel('image'),
  ]


