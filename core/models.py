from django.db import models


class Campaign(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=100)
    description = models.TextField(verbose_name="Description", null=True, default=None)
    is_active = models.BooleanField(verbose_name="Est active", default=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def response_count(self):
        return Response.objects.filter(question__campaign=self).count()

    def questions(self):
        return Question.objects.filter(campaign=self)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Campagne"


class Question(models.Model):
    campaign = models.ForeignKey(Campaign, null=True, on_delete=models.SET_NULL)
    question = models.CharField(verbose_name="Question", max_length=250)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def responses(self):
        return Response.objects.filter(question=self)

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = "Question"


class Response(models.Model):
    THEMES = (
        ('btn-primary', 'BLEU'),
        ('btn-danger', 'ROUGE'),
        ('btn-warning', 'JAUNE'),
        ('btn-info', 'BLEU CIEL'),
        ('btn-dark', 'SOMBRE'),
        ('btn-light', 'CLAIR'),
        ('btn-pink', 'ROSE')
    )

    FONT_SIZES = (
        ('fs-6', 'Font 1'),
        ('fs-5', 'Font 2'),
        ('fs-4', 'Font 3'),
        ('fs-3', 'Font 4'),
        ('fs-2', 'Font 5'),
        ('fs-1', 'Font 6'),
        ('fs-0', 'Font 7'),
    )

    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    theme = models.CharField(verbose_name="Theme", max_length=20, choices=THEMES, default=THEMES[0][0])
    font_size = models.CharField(verbose_name="Font Size", max_length=20, choices=FONT_SIZES, default=FONT_SIZES[0][0])
    response = models.CharField(verbose_name="Reponse", max_length=100)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.response}"

    class Meta:
        verbose_name = "Reponse"


class Reply(models.Model):
    response = models.ForeignKey(Response, null=True, on_delete=models.SET_NULL)
    value = models.IntegerField(verbose_name='Valeur', default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Répondre à la question"
