from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

from manager.forms import AdminCreateForm, FeeForm, MemberForm, TrainerForm, SearchForm
from manager.models import Admin, Member, Fee, Trainer

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact_us.html'


class AdminDash(LoginRequiredMixin, TemplateView):
    template_name = 'admin_dash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['member_count'] = Member.objects.all().count()
        context['trainer_count'] = Trainer.objects.all().count()
        context['daily_member_count'] = Member.objects.all().filter(
            date_joined__gte=datetime.date.today() - datetime.timedelta(30)).count()

        mem_objs = Member.objects.filter(
            date_joined__lte=timezone.now()).order_by('-date_joined')[0:2]
        m0_username = mem_objs[0].username
        m0_date = mem_objs[0].date_joined
        m0_email = mem_objs[0].email
        m1_username = mem_objs[1].username
        m1_date = mem_objs[1].date_joined
        m1_email = mem_objs[1].email

        context['m0_username'] = m0_username
        context['m0_date'] = m0_date.date()
        context['m0_email'] = m0_email
        context['m1_username'] = m1_username
        context['m1_date'] = m1_date.date()
        context['m1_email'] = m1_email

        tra_objs = Trainer.objects.filter(
            date_joined__lte=timezone.now()).order_by('-date_joined')
        t0_username = tra_objs[0].username
        t0_date = tra_objs[0].date_joined
        t0_email = tra_objs[0].email
        t1_username = tra_objs[1].username
        t1_date = tra_objs[1].date_joined
        t1_email = tra_objs[1].email

        context['t0_username'] = t0_username
        context['t0_date'] = t0_date.date()
        context['t0_email'] = t0_email
        context['t1_username'] = t1_username
        context['t1_date'] = t1_date.date()
        context['t1_email'] = t1_email

        return context


class CreateAdmin(LoginRequiredMixin, CreateView):
    template_name = 'admin_form.html'
    form_class = AdminCreateForm
    success_url = reverse_lazy('adminDash')


class CreateMember(LoginRequiredMixin, CreateView):
    template_name = 'member_form.html'
    model = Member
    form_class = MemberForm


class ViewAllMembers(LoginRequiredMixin, ListView):
    model = Member
    template_name = 'member_list.html'
    context_object_name = 'member_info'

    def get_queryset(self):
        return Member.objects.filter(date_joined__lte=timezone.now()).order_by('-date_joined')


class ViewsDetailMember(LoginRequiredMixin, DetailView):
    model = Member
    context_object_name = 'member_info_detail'
    template_name = 'member_detail.html'


class UpdateMemberDetails(LoginRequiredMixin, UpdateView):
    form_class = MemberForm
    model = Member
    template_name = 'member_form.html'


class DeleteMemberDetails(LoginRequiredMixin, DeleteView):
    form_class = MemberForm
    model = Member
    template_name = 'member_confirm_delete.html'
    success_url = reverse_lazy('manager:memberlist')


class CreateTrainer(LoginRequiredMixin, CreateView):
    template_name = 'trainer_form.html'
    model = Trainer
    form_class = TrainerForm


class ViewAllTrainers(LoginRequiredMixin, ListView):
    model = Trainer
    template_name = 'trainer_list.html'
    context_object_name = 'trainer_info'

    def get_queryset(self):
        return Trainer.objects.filter(date_joined__lte=timezone.now()).order_by('-date_joined')


class ViewsDetailTrainer(LoginRequiredMixin, DetailView):
    model = Trainer
    context_object_name = 'trainer_info_detail'
    template_name = 'trainer_detail.html'


class UpdateTrainerDetails(LoginRequiredMixin, UpdateView):
    form_class = TrainerForm
    model = Trainer
    template_name = 'trainer_form.html'


class DeleteTrainerDetails(LoginRequiredMixin, DeleteView):
    form_class = TrainerForm
    model = Trainer
    template_name = 'trainer_confirm_delete.html'


class CreateFee(CreateView):
    form_class = FeeForm
    model = Fee
    template_name = 'fee_form.html'

###########################################################
###########################################################
###########################################################


@login_required
def SearchMember(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.process()
            data = data['data']

            all_data = Member.objects.filter(username__contains=data)

    return render(request, 'member_list.html', {'member_info': all_data})


@login_required
def SearchTrainer(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.process()
            data = data['data']

            all_data = Trainer.objects.filter(username__contains=data)

    return render(request, 'trainer_list.html', {'trainer_info': all_data})
