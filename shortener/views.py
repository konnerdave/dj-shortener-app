from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from shortener.models import URL
from shortener.forms import URLForm
from shortener.helpers.shortener import Shortener


class IndexView(View):
    """
        View to Handle URL Form 
    """

    def get(self, request):
        form = URLForm()
        return render(request, 'shortener/index.html', {'form': form})

    def post(self, request):
        form = URLForm(request.POST)
        token = ''

        if form.is_valid():
            new_url = form.save(commit=False)
            
            # If the hash isn't provided
            if not new_url.url_hash:
                # Issue and set a new token
                token = Shortener().issue_token()
                new_url.url_hash = token
            
            new_url.save()
            context = {
                'form': form,
                'new_url': new_url.url_hash,
                'success': 'Successfully created'
            }

        else:
            errors = form.errors
            form = URLForm()
            context = {
                'form': form,
                'errors': errors,
            }

        return render(request, 'shortener/index.html', context)


class HomeView(View):
    """
        View to Redirect from shortened URL 
    """

    def get(self, request, token):
        try:
            url = URL.objects.get(url_hash=token)
            return redirect(url.full_url)
        except:
            return HttpResponseRedirect(reverse('index'))
