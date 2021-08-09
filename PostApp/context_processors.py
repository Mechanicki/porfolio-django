from .models import Post_comments

def extras(request):
    comments = Post_comments.objects.all()
    return {'comments':comments}