from django.shortcuts import render, redirect
from django.views.generic import FormView, View
from appFellas.forms import UploadImageForm, AuthorizationForm
from appFellas.models import Image, User


class UploadImageView(FormView):
    template_name = 'new_image.html'
    form_class = UploadImageForm

    def get(self, request, *args, **kwargs):
        if request.session.get('user_e_mail'):
            form = self.get_form(UploadImageView.form_class)
            return render(request, UploadImageView.template_name, {'form': form})
        else:
            return redirect('/authorization')

    def post(self, request, *args, **kwargs):
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            author_e_mail = request.session.get('user_e_mail')
            author = User.objects.filter(e_mail=author_e_mail).first()
            instance = Image(image=request.FILES['image'], author=author)
            instance.save()
            return redirect('/')
        return render(request, 'new_image.html', {'error': 'error in validation', 'form': UploadImageForm})


class AuthorizationView(FormView):
    template_name = 'authorization.html'
    form_class = AuthorizationForm

    def get(self, request, *args, **kwargs):
        if request.session.get('user_e_mail'):
            return redirect('/')
        else:
            form = self.get_form(AuthorizationView.form_class)
            return render(request, AuthorizationView.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        authorization_form = AuthorizationForm(request.POST)
        if authorization_form.is_valid():
            user_e_mail = authorization_form.cleaned_data['e_mail']
            user_password = authorization_form.cleaned_data['password']
            u = User.objects.filter(e_mail=user_e_mail, password=user_password).first()
            if u is not None:
                request.session['user_e_mail'] = u.e_mail
                return redirect('/')
            else:
                return render(request, 'authorization.html', {'error': 'authorization incorrect',
                                                              'form': AuthorizationForm})


class GetImagesView(View):
    template_name = 'images.html'

    def get(self, request):
        return render(request, 'images.html', {})


class LogOutView(View):
    template_name = 'index.html'

    def get(self, request):
        request.session.clear()
        return redirect('/')
