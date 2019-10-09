from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostFormDetail
from django.views import View as djviews
from .models import UserDataDetail,MultipleImg
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

@method_decorator(login_required, name='dispatch')
class DisplayImages(ListView):

    def get(self, request):
        User_list = UserDataDetail.objects.filter(user=request.user)

        return render(self.request, 'pic.html', {'data':User_list })


class UserDataDet(CreateView):
    model = UserDataDetail
    fields = ['user','title', 'description','image']

    def get(self, request,pk):
        detail = UserDataDetail.objects.get(id=pk)
        return render(request,'details.html',{'detail':detail})


@method_decorator(login_required, name='dispatch')
class BasicUploadView(djviews):
    def get(self, request):
        User_Data =PostFormDetail()
        return render(self.request, 'data.html', {'data':User_Data })

    def post(self, request,):
        form = PostFormDetail(self.request.POST,self.request.FILES)
        pic = request.FILES.getlist('image')
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            for i in pic:
                pictures = MultipleImg(name = form, picture= i)
                pictures.save()

            return redirect('home')


class UserDetailUpdate(UpdateView): 
    model = UserDataDetail
    success_url = reverse_lazy('home') 
    fields = ['title', 'description','image']


class UserDetailDelete(DeleteView): 
    model = UserDataDetail
    success_url = reverse_lazy('home')

