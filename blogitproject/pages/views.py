from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
from profiles.models import Profile
from taggit.models import Tag
from django.core.paginator import Paginator

# Create your views here.
@login_required
def index(request):
    blogs = Blog.objects.filter(is_published=True).order_by('-created_at')
    profile = Profile.objects.get(user=request.user)
    latest_blogs = blogs[:4]

    tags = Tag.objects.all()

    get_params = '' # параметр фильтрации и сортировки для Pagination

    if request.method == 'GET':
        search = request.GET.get('search', '')
        if search:
            blogs = blogs.filter(text__icontains=search)
            get_params += '&search={0}'.format(search)
        
        sort_by = request.GET.get('sort_by', '')
        if sort_by:
            sort_by_dict = {
                'a-z': 'title',
                'z-a': '-title',
                'new-old': '-created_at',
                'old-new': 'created_at'
            }
            sort_by_param = sort_by_dict.get(sort_by)
            blogs = blogs.order_by(sort_by_param)
            get_params += '&sort_by={0}'.format(sort_by)
        
        filter_by_tag = request.GET.get('filter_by_tag', '')
        if filter_by_tag:
            blogs = blogs.filter(tags__name__icontains=filter_by_tag)
            get_params += '&filter_by_tag={0}'.format(filter_by_tag)
    
    # Paginator
    paginator = Paginator(blogs, 2) # Show 2 blogs per page.
    page_number = request.GET.get('page') # если страницу не передают будет None
    page_obj = paginator.get_page(page_number)

    context = {
        # 'blogs': blogs,
        'profile': profile,
        'latest_blogs': latest_blogs,
        'tags': tags,
        'page_obj': page_obj,
        'get_params': get_params,
    }
    return render(request, 'pages/index.html', context=context)