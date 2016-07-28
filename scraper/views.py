# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from .models import Link, Site
from .serializers import SiteSerializer, LinkSerializer

import pdb


class IndexView(generic.ListView):
    template_name = 'scraper/index2.html'
    context_object_name = 'top_news'

    def get_queryset(self):
        """Return the last five published questions."""
        return Site.objects.filter().order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Site
    template_name = 'scraper/detail2.html'
    # def get_queryset(self):
    # 	return Site.objects.filter().order_by("-id")

#objects
    # latest_coord_list = Coordinates.objects.order_by('-pub_date')[:1]
    # context = {"form":form, "latest_coord_list":latest_coord_list}
    
def voteUp(request):
    selected_site=get_object_or_404(Site, pk=request.POST.get('voteUp', False))
    selected_site.site_vote +=1
    selected_site.save()
    return HttpResponseRedirect(reverse('scraper:detail', args=(selected_site.id,)))

def voteDown(request):
    selected_site=get_object_or_404(Site, pk=request.POST.get('voteDown', False))
    selected_site.site_vote -=1
    selected_site.save()
    return HttpResponseRedirect(reverse('scraper:detail', args=(selected_site.id,)))

def updateSite(request):
    selected_site=get_object_or_404(Site, pk=request.POST.get('updateSite', False))
    selected_site.save()
    if(selected_site.site_text == "Daily Bruin"):
            s = selected_site
            s.save()
            r = requests.get("http://www.dailybruin.com/category/news/")
            page_text = r.text.encode('utf-8').decode('ascii', 'ignore')
            page_soupy = BeautifulSoup(page_text)
            g_data = page_soupy.find_all("div",{"class":"row db-list"})
            ##db complete loop
            g_articles = page_soupy.find_all("div",{"class": "entry-content"})
            for x in xrange(0,5):
                try: 
                    ##db html
                    db_str = "http://www.dailybruin.com"
                    db_link = db_str + g_articles[x].find_all("a")[0].get('href')
                    l_html = db_link
                    ##db title
                    l_text = g_data[x].find_all("h2")[0].text.encode('utf-8').decode('ascii', 'ignore')
                    ##db body
                    l_body = g_data[x].find_all("p")[0].text.encode('utf-8').decode('ascii','ignore')
                    if l_body.endswith('Read more... '):
                        l_body=l_body[:-13]

                    s.sitelink_set.create(title = l_text, content = l_body, address = l_html)
                    s.pub_date = timezone.now()
                    s.save()
                except:
                    pass
    if(selected_site.site_text == "Christian Science Monitor"):
        s = selected_site
        s.save()
        r = requests.get("http://www.csmonitor.com")
        page_text = r.text.encode('utf-8').decode('ascii', 'ignore')
        page_soupy = BeautifulSoup(page_text)
        g_data = page_soupy.find_all("div",{"class":"story_block_item"})
        ##csmonitor complete loop
        for x in xrange(8,13):
            l_text = g_data[x].find_all("a")[0].text.encode('utf-8').decode('ascii', 'ignore')
            l_content = g_data[x].find_all("p")[0].text.encode('utf-8').decode('ascii', 'ignore')
            if l_text and l_content:
                try:
                    l_str = "http://www.csmonitor.com"
                    l_html = l_str + g_data[x].find_all("a")[0].get('href')
                    s.sitelink_set.create(title = l_text, content = l_content, address = l_html)
                    s.pub_date = timezone.now()
                    s.save()
                except:
                    print "fail"
                    pass
    if(selected_site.site_text == "Engadget"):
        s = selected_site
        s.save()
        r = requests.get("http://www.engadget.com")
        page_text = r.text.encode('utf-8').decode('ascii', 'ignore')
        page_soupy = BeautifulSoup(page_text)
        g_data = page_soupy.find_all("article",{"class":"o-hit"})
        ##csmonitor complete loop
        for x in xrange(5,10):
            try:
                l_text = g_data[x].find_all("h2")[0].text.encode('utf-8').decode('ascii', 'ignore')
                l_content = g_data[x].find_all("p")[0].text.encode('utf-8').decode('ascii', 'ignore')
                l_str = "http://www.engadget.com"
                l_html = l_str + g_data[x].find_all("a",{"class":"o-hit__link"})[0].get('href')
                s.sitelink_set.create(title = l_text, content = l_content, address = l_html)
                s.pub_date = timezone.now()
                s.save()
            except:
                print "fail"
                pass
    return HttpResponseRedirect(reverse('scraper:detail', args=(selected_site.id,)))

# GET: returns 5 most recent articles for dailybruin
# UPDATE: updates 5 most recent articles for dailybruin
@api_view(['GET'])
def dailybruin(request):
    site = Site.objects.get(name="Daily Bruin")
    if request.method == 'GET':
        updateDailyBruin()
        # return HttpResponse('I\'m a teapot short and stout.', status=418)
        return HttpResponseRedirect(reverse('scraper:detail', args=(site.id,)))

@api_view(['GET']) 
def csmonitor(request):
    site = Site.objects.get(name="Christian Science Monitor")
    if request.method == 'GET':
        updateCSMonitor()
        # return HttpResponse('I\'m a teapot short and stout.', status=418)
        return HttpResponseRedirect(reverse('scraper:detail', args=(site.id,)))

@api_view(['GET']) 
def engadget(request):
    site = Site.objects.get(name="Engadget")
    if request.method == 'GET':
        updateEngadget()
        return HttpResponseRedirect(reverse('scraper:detail', args=(site.id,)))

# @api_view(['GET']) 
# def YCombinator(request):
#     site = Site.objects.get(name="YCombinator")
#     updateYCombinator()
#     return HttpResponse('I\'m a teapot short and stout.', status=418)

#SITE METHODS
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
#no return
def updateDailyBruin():
    s = Site.objects.get(name="Daily Bruin")
    r = requests.get("http://www.dailybruin.com/category/news/")
    page_text = r.text.encode('utf-8').decode('ascii', 'ignore')
    page_soupy = BeautifulSoup(page_text)
    g_data = page_soupy.find_all("div",{"class":"row db-list"})
    ##db complete loop
    g_articles = page_soupy.find_all("div",{"class": "entry-content"})
    for x in xrange(0,5):
        try: 
            ##db html
            db_str = "http://www.dailybruin.com"
            db_link = db_str + g_articles[x].find_all("a")[0].get('href')
            l_html = db_link
            ##db time
            l_time = g_data[x].find_all("h5")[0].text.encode('utf-8').decode('ascii','ignore')
            ##db title
            l_text = g_data[x].find_all("h2")[0].text.encode('utf-8').decode('ascii', 'ignore')
            ##db body
            l_body = g_data[x].find_all("p")[0].text.encode('utf-8').decode('ascii','ignore')

            if l_body.endswith('Read more... '):
                l_body=l_body[:-13]
            s.link_set.create(title=l_text, content=l_body, address=l_html, pub_date=timezone.now())
            s.save()
            data = {"title": l_text, "content":l_body, "address":l_html, "pub_date":l_time}
            # serializer = LinkSerializer(data=data, partial=True)
            # serializer.save()
        except:
            pass
    s.updateDate()
    return

###csmonitor
def updateCSMonitor():
    site = Site.objects.get(name="Christian Science Monitor")
    r = requests.get("http://www.csmonitor.com")
    page_text = r.text.encode('utf-8').decode('ascii', 'ignore')
    page_soupy = BeautifulSoup(page_text)
    g_data = page_soupy.find_all("div",{"class":"story_block_item"})
    ##csmonitor complete loop
    # reverse order to get the top links to show on top.
    for x in reversed(xrange(5)):
        l_text = g_data[x].find_all("span",{"class":"story_link"})[0].text.encode('utf-8').decode('ascii', 'ignore')
        l_content = g_data[x].find_all("p", {"class":"story_summary"})[0].text.encode('utf-8').decode('ascii', 'ignore')
        if l_text and l_content:
            try:
                l_str = "http://www.csmonitor.com"
                l_html = l_str + str(g_data[x].find_all("a")[0].get('href'))
                l_text = str(l_text.strip())
                l_content = str(l_content.strip()) 
                site.link_set.create(title=l_text, content=l_content, address=l_html, pub_date = timezone.now())
                site.save()
            except:
                print "fail"
                pass
    site.updateDate()
    return

def updateEngadget():
    site = Site.objects.get(name="Engadget")
    r = requests.get("http://www.engadget.com")
    page_text = r.text.encode('utf-8').decode('ascii', 'ignore')
    page_soupy = BeautifulSoup(page_text)
    g_latest = page_soupy.find_all("div", {"class":"grid@tl+ pt-40@tp+ flex@tl+"})
    g_articles = g_latest[0].find_all("article", {"class":"o-hit"})

    ##csmonitor complete loop
    for x in reversed(xrange(5)):
        try:
            l_text = g_articles[x].find_all("div", {"class":"th-title"})[0].text.encode('utf-8').decode('ascii', 'ignore')
            l_content = g_articles[x].find_all("p")[0].text.encode('utf-8').decode('ascii', 'ignore')
            # l_content = g_articles[x].find_all("div", {"class":"hide@s mt-10@s"})[0].text.encode('utf-8').decode('ascii', 'ignore')
            l_str = "http://www.engadget.com"
            # g_title = g_articles[x].find_all("div", {"class":"th-title"})
            l_html = l_str + g_articles[x].find_all("a", {"class":"o-hit__link"})[0].get('href')
            l_text = str(l_text.strip())
            l_content = str(l_content.strip())
            site.link_set.create(title = l_text, content = l_content, address = l_html, pub_date=timezone.now())
            site.save()
        except:
            print "fail"
            pass
    site.updateDate()
    return

#about me
def aboutme(request):
    return render(request, 'scraper/aboutme.html')