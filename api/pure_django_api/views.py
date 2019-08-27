from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll


def polls_list(request):
    polls = Poll.objects.all()[:10]
    data = {"results": list(polls.values('pk', "question", "created_by", 'pub_date'))}
    # These are model fields
    # using the list serializes the data.
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"detail_of_specific_poll": {
        "related_to_question": poll.question,
        "Poll_created_by": poll.created_by,
        "created_on": poll.pub_date
    }}
    return JsonResponse(data)