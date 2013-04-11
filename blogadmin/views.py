from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import PostForm

from blog.models import Post


class LoginRequiredMixin(object):
    """Ensures that user must be authenticated in order to access view."""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class BaseAdminView(LoginRequiredMixin, View):
    """ Base class view for admin views """
    class Meta:
        abstract = True


################################################################################
##### Copy following classes per model #########################################
################################################################################


### Post
##################################
class BasePostView(BaseAdminView):
    """ Base class view for all post admin views. """
    class Meta:
        abstract = True

    def get_context_data(self, *args, **kwargs):
        context = super(BasePostView, self).get_context_data(*args, **kwargs)
        context['section'] = 'post'
        context['model_name'] = 'Post'
        context['models_name'] = 'Posts'
        return context

    model = Post


class BasePostEditView(BasePostView):
    """ Base class view for post editing views. """
    class Meta:
        abstract = True

    form_class = PostForm
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('list_post')


class ListPost(BasePostView, ListView):
    """ List the posts in a table for its edition/deletion or creating
    new ones. """
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

list_post = ListPost.as_view()


class CreatePost(BasePostEditView, CreateView):
    """ Creates a new post. """
    template_name = 'post/post_create.html'

create_post = CreatePost.as_view()


class EditPost(BasePostEditView, UpdateView):
    """ Edits an existing post. """
    template_name = 'post/post_create.html'

edit_post = EditPost.as_view()


class DeletePost(BasePostEditView, DeleteView):
    """ Deletes an existing post. """
    template_name = 'post/post_confirm_delete.html'

delete_post = DeletePost.as_view()
