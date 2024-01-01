from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import BlogModel, Category
from django.core.paginator import Paginator
from django.db.models import Q


class BlogView(ListView):
    template_name = 'blog/blog.html'
    model = BlogModel
    paginate_by = 4

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return BlogModel.objects.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(slug__icontains=q))
        return BlogModel.objects.all()

    # def get_queryset(self):
    #     category_pk = self.kwargs.get('pk')
    #     if category_pk:
    #         category = get_object_or_404(Category, id=category_pk)
    #         return category.blogs.all()
    #     return BlogModel.objects.all()


class DetailView(DetailView):
    model = BlogModel
    template_name = "blog/detail.html"


def category_view(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    result = category.blogs.all()
    page_number = request.GET.get("page")
    paginate = Paginator(result, 5)
    objects = paginate.get_page(page_number)
    return render(request, "blog/blog.html", {"object_list": objects})