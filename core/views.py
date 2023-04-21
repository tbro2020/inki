from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import View
from django.apps import apps

CampaignModel = apps.get_model("core", model_name="campaign")


class Home(View):
    def get(self, request):
        qs = CampaignModel.objects.filter(is_active=True)
        return render(request, "home.html", locals())


class Campaign(View):
    def get(self, request, pk):
        obj = get_object_or_404(CampaignModel, pk=pk)
        return render(request, "campaign.html", locals())

    def post(self, request, pk):
        obj = get_object_or_404(CampaignModel, pk=pk)
        messages.add_message(request, level=messages.SUCCESS, message="Thank your for your feedback")
        return redirect(reverse('core:campaign', kwargs={'pk': pk}))


class Report(View):
    def get(self, request, pk):
        print(request.data)
        return render(request, "report.html", locals())
