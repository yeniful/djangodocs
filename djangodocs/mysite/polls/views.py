from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(reqest, question_id):
    reponse = "Yor're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)   