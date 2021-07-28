from django.shortcuts import render

posts = [
    {
        'author': 'Damian',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date': '28.07.2021',
    },
    {
        'author': 'Pawel',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date': '29.07.2021',
    },
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Dummy title'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
