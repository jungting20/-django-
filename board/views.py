from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from board.models import Board
from board.forms import BoardForm


class Boardlistview(ListView):
    template_name = 'boardlist.html'
    context_object_name = 'boardlist'
    paginate_by = 3


    def get_context_data(self, **kwargs):
        context = super(Boardlistview,self).get_context_data(**kwargs)
        return context

    # 오 이걸로 바꾸는 듯
    #여기서 self.request메서드로 조지는거임 빡시네
    def paginate_queryset(self, queryset, page_size):
        print('뭐여',self.request.GET['page'])
        return super().paginate_queryset(queryset, 2)

    def get_queryset(self):

        return Board.objects.order_by('-created_at')


class BoardDetailview(DetailView):
    model = Board
    template_name = 'detail.html'



@login_required()
def boardwirte(request):

    if request.method == "POST":
        form = BoardForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj = form.save()
            return redirect(obj)
    else:
        form = BoardForm()
        return render(request,'boardwrite.html',context={
        'form':form
    })


        
