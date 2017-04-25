#!/usr/bin/env python2

from verdandi.verdandi import Verdandi
from verdandi.modules.page import Page
from verdandi.modules.commonassets import CommonAssets
from verdandi.modules.newsfeed import NewsFeed
from verdandi.modules.gallery import Gallery
from verdandi.modules.sassassets import SassAssets

class TestPage1(Page):
	menu_title = "New Page"
	menu_label = "new_cool_page"

class TestPage2(Page):
	assets = [('img/foo.png', 'img/'),
				('img/foo.png', 'img/bar.png'),
				('img/foo.png', 'img/bar')]
	url = "page2.html"
	menu_title = "Other new Page"
	menu_label = "cool_page1"
	content_file = "content_other.md"
	news_feed_id = "news"


class TestPage3(Page):
	menu_title = "Other new Page2"
	menu_label = "cool_page2"
	menu_parent = "cool_page1"
	url = "subdir/page3.html"
	content_file = "content_yetanother.md"
	news_feed_id = "news"

	metadata = {
		'image' : 'img/bar.png',
	}

class Assets(CommonAssets):
	assets = [('img', 'img/dir'),
				('img/', 'img/files')]


class Styles(SassAssets):
	assets = [('test.scss', 'css/test.css'),]

class News(NewsFeed):
	title = "New News"
	url = "news.html"
	menu_title = "News"
	menu_label = "news"
	news_feed_id = "news"
	metadata = {
		'description' : 'A news feed with news',
		'image' : 'img/bar.png',
	}

class TestGallery(Gallery):
	url = "testgallery.html"
	gallery_directory = "test_gallery"
	gallery_images_url = "img/test_gallery"


class TestBlog(Verdandi):
	modules = [TestPage1(),
				TestPage2(),
				TestPage3(),
				Assets(),
				Styles(),
				News(),
				TestGallery()]


testblog = TestBlog()
testblog.run()
