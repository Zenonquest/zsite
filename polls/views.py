from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class QuestionView(generic.ListView):
    template_name = 'polls/question.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'
    def get_queryset(self):
    	return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

def vote(request, question_id):
	p=get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form.
		return render(request, 'polls/details.html',{
			'question': p,
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.vote +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

# def about_page(request):
# 	return render(request, 'polls/about.html')

# def thanks_page(request):
# 	return render(request, 'polls/thanks.html')

# def blog_page(request):
# 	return render(request, 'polls/blog.html')

# def questions_page(request):
# 	return render(request, 'polls/questions.html')

# def contacts_page(request):
# 	return render(request, 'polls/contacts.html')