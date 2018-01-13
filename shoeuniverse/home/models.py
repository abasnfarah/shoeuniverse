from __future__ import absolute_import, unicode_literals

from django.db import models
from django.shortcuts import render

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey

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

  content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    InlinePanel('style_tiles', label="Styles"),
  ]

class ShoeTile(models.Model):
  # Define objects within the tile (title, image, link)
  embed_url = models.URLField("Embed URL", blank=True)
  title = models.CharField(max_length=255, blank=True)

  # Define panel (similar to content_panel of a Page)
  panel = [
    FieldPanel('title'),
    FieldPanel('embed_url'),
  ]

  class Meta:
    abstract = True
    verbose_name = "Tile"
    verbose_name_plural = "Tiles"

class HomeShoeTile(Orderable, ShoeTile):
  page = ParentalKey(HomePage, related_name='shoe_tiles')

class StyleShoeTile(Orderable, ShoeTile):
  page = ParentalKey(ShoeHistoryPage, related_name='style_tiles')


