from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from  . import models
from django.views import generic


class index(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return models.Question.objects.order_by('-date')[:5]





def detail(request, question_id):
    que = get_object_or_404(models.Question, id = question_id )

    context = {
    'que' : que
    }

    return render(request, 'poll/detail.html', context)
    #return HttpResponse("You're looking at question %s." % question_id)




def result(request, question_id):
    question = get_object_or_404(models.Question, id=question_id)

    return render(request, 'poll/result.html', {'question': question})





def vote(request, question_id):
    que = get_object_or_404(models.Question, id=question_id)
    context = {
    'que' : que,
    'error_message' : "choice is not avibail"
    }
    try:
        selected_choice = que.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', context)
    else:
        selected_choice.vots += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:result', args=(que.id,)))
