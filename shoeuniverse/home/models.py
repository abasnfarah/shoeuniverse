from __future__ import absolute_import, unicode_literals

from django.db import models
from django.shortcuts import render

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel

from modelcluster.fields import ParentalKey

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class ShoeHistoryPage(Page):
		body = RichTextField(blank=True)

		content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('style_tiles', label="Styles"),
    ]

class ShoeTile(models.Model):
	class Meta:
		verbose_name = "Tile"
		verbose_name_plural = "Tiles"

class HomeShoeTile(Orderable, ShoeTile):
	pass

class StyleShoeTile(Orderable, ShoeTile):
	page = ParentalKey(ShoeHistoryPage, related_name='style_tiles')


