import datetime
from django.db import models
from django.utils import timezone
#web scraper shell imports
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your models here.
class Site(models.Model):
	# site_text should be site_name
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	site_vote = models.IntegerField(default=0)
	def __str__(self):
		return self.site_text

	def updateDate(self):
		self.pub_date = timezone.now()
		self.save()

	#Voting for site
	def upVote(self):
		self.site_vote = self.site_vote + 1
		self.save()
		return HttpResponseRedirect(reverse('scraper:index'))
	def downVote(self):
		self.site_vote = self.site_vote - 1
		self.save()
		return HttpResponseRedirect(reverse('scraper:index'))
	#updates page
	# def nextFive(self):
	# 	s = self
	# 	s.save()
	# 	r = requests.get("http://www.dailybruin.com/category/news/")
	# 	page_text = r.text.encode('utf-8').decode('ascii', 'ignore')
	# 	page_soupy = BeautifulSoup(page_text)
	# 	g_data = page_soupy.find_all("div",{"class":"row db-list"})
	# 	##db complete loop
	# 	g_articles = page_soupy.find_all("div",{"class": "entry-content"})
	# 	for x in xrange(0,5):
	# 		try: 
	# 			##db html
	# 			db_str = "http://www.dailybruin.com"
	# 			db_link = db_str + g_articles[x].find_all("a")[0].get('href')
	# 			l_html = db_link
	# 			##db title
	# 			l_text = g_data[x].find_all("h2")[0].text.encode('utf-8').decode('ascii', 'ignore')
	# 			##db body
	# 			l_body = g_data[x].find_all("p")[0].text.encode('utf-8').decode('ascii','ignore')
	# 			if l_body.endswith('Read more... '):
	# 				l_body=l_body[:-13]

	# 			s.sitelink_set.create(link_text = l_text, link_content = l_body, link_html = l_html)
	# 			s.save()
	# 		except:
	# 			pass
	# 	return HttpResponseRedirect(reverse('scraper:index'))
		

##Object for each individual link in the website
class Link(models.Model):
	site = models.ForeignKey(Site)
	# link_text should be title
	title = models.CharField(max_length=2000)
	content = models.TextField(max_length=200000)
	address = models.TextField(max_length=20000)
	pub_date = models.DateTimeField(blank=True, null=True)
	vote = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title

	def upVote(self):
		self.vote = self.vote + 1
		self.save()
		# return HttpResponseRedirect(reverse('scraper:index'))

	def downVote(self):
		self.site_vote = self.site_vote - 1
		self.save()
		# return HttpResponseRedirect(reverse('scraper:index'))

	class Meta:
		ordering = ['-pub_date']

