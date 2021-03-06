from django.db import models

# Create your models here.
class Work(models.Model):

    title = models.CharField(max_length=63)
    subtitle = models.CharField(max_length=63)

    def __str__(self):
        return "{0} : {1} {2}".format(self.id, self.title, self.subtitle)


class Portfolio(models.Model):

    PLANET_SIZES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('big', 'Big'),
    ]

    name = models.CharField(max_length=63)
    #homepage = models.CharField(max_length=7, null=True, blank=True)

    energy = models.SmallIntegerField(default=1)
    planet_size = models.CharField(max_length=63, choices=PLANET_SIZES, null=True, default=PLANET_SIZES[0][0])

    image = models.ImageField(upload_to="images/portfolio/")
    alt_image = models.TextField(max_length=255)

    link = models.URLField()
    label_link = models.CharField(max_length=63)

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=63, null=True, blank=True)
    subtitle = models.CharField(max_length=63, null=True, blank=True)

    description = models.TextField(max_length=255, null=True, blank=True)

    online = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if self.energy == None:
            self.energy = 0

        if other.energy == None:
            other.energy = 0

        return float(self.energy) < float(other.energy)

    def get_portfolio_type(self):
        return 'BASE'

    @staticmethod
    def get_all_portfolios():

        portfolios = []
        portfolios_classnames = [
            'WorkPortfolio',
            'MuggumPortfolio',
            'InstagramPortfolio',
        ]

        for classname in portfolios_classnames:
            portfolio = eval(classname)
            if portfolio.objects.first() != None:
                try:
                    for item in portfolio.objects.filter(online=True).order_by('-energy').all():
                        portfolios.append(item)
                except:
                    for item in portfolio.objects.filter(online=True).all():
                        portfolios.append(item)

        return portfolios

class InstagramPortfolio(Portfolio):

    insta_id = models.CharField(max_length=63, null=True, blank=True)
    photo_id = models.CharField(max_length=63, null=True, blank=True)

    def get_portfolio_type(self):
        return 'INSTA'

class WorkPortfolio(Portfolio):

    work = models.ForeignKey(Work, on_delete=models.SET_NULL, null=True)

    def get_portfolio_type(self):
        return 'WORK'

class MuggumPortfolio(Portfolio):

    work = models.ForeignKey(Work, on_delete=models.SET_NULL, null=True)

    def get_portfolio_type(self):
        return 'MUGGUM'
