from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView
from news.models import Topic, Tag
from users.models import Author
from .forms import ArticleUrlForm, ArticleForm

from newspaper import Article as SmartArticle


class TopicCreateView(CreateView):
    model = Topic
    fields = ['name']
    success_url = '/news/'


class TagCreateView(CreateView):
    model = Tag
    fields = ['article_id', 'name']
    success_url = '/news/'


# class UrlCreateView(CreateView):
#     model = Article_URL
#     fields = ['url']
#     success_url = '/news/'


# class ArticleUrlFormView(FormView):
#     template_name = 'news_admin/article_url_form.html'
#     form_class = ArticleUrlForm
#     success_url = reverse_lazy('article-from-url')


class ArticleFromUrlCreateView(CreateView):
    template_name = 'news_admin/article_url_form.html'
    form_class = ArticleForm

    def post(self, request, *args, **kwargs):
        super(ArticleFromUrlCreateView, self).post(request)
        if request.POST['article-url']:
            return HttpResponse(request.POST['article-url'])
        else:
            return HttpResponse("Did not get url")

    def get_initial(self):
        return {
            'author': self.request.user,
        }


def article_url(request):
    form = ArticleUrlForm()
    return render(request, 'news_admin/article_url_form.html', {'form': form})


def article_from_url(request):
    if request.method == 'POST':
        article_url = request.POST.get('article_url', None)
        form = ArticleForm(request.POST.copy())
        print("here")
        # Pre-populate form with content from article url (if exists)
        if article_url is not None:
            filler = SmartArticle(article_url)
            filler.download()
            filler.parse()
            filler.nlp()

            form.data['headline'] = filler.title
            form.data['datetime'] = filler.publish_date
            form.data['image_url'] = filler.top_image
            form.data['content'] = filler.text
            form.data['article_url'] = article_url
            print(str(filler.keywords))
            form.data['keywords'] = str(filler.keywords)
            print("here2")

            if form.is_valid():
                form = form.save(commit=False)
                form.author = Author.objects.filter(user=request.user)[0]
                form.save()
                return redirect('news-home')
            return render(request, 'news_admin/topic_form.html', {'form': form})

        # return render(request, 'news_admin/topic_form.html', {'form': form})
    else:
        print("Blank Form")
        form = ArticleForm()
        return render(request, 'news_admin/topic_form.html', {'form': form})

