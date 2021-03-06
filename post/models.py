from django.db import models 
from django.contrib.auth.models import User 
from tagging.fields import TagField 
from markdown import markdown 
import datetime 

# Create your models here.
class Category(models.Model): 
    title = models.CharField(max_length=250, help_text="Maximum 250 characters.") 
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.") 
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"	
	
    def __unicode__(self): 
        return self.title 

    def get_absolute_url(self): 
        return "/categories/%s/" % self.slug
		
		
class Post(models.Model):
    LIVE_STATUS = 1 
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3   	
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'), 
        (DRAFT_STATUS, 'Draft'), 
        (HIDDEN_STATUS, 'Hidden'),
	)
	
    # Core Fields 
    title = models.CharField(max_length=250) 
    excerpt = models.TextField(blank=True) 
    body = models.TextField() 
    pub_date = models.DateTimeField(default=datetime.datetime.now) 
	
    # Fields to store the generated html 
    excerpt_html = models.TextField(editable=False, blank=True) 
    body_html = models.TextField(editable=False, blank=True)
	
    # Meta Info 
    author = models.ForeignKey(User) 
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS) 
    slug = models.SlugField(unique_for_date='pub_date') 
	
    # Categorization 
    categories = models.ManyToManyField(Category) 
    tags = TagField(help_text="Separate tags with spaces") 

    class Meta: 
        ordering = ['-pub_date']	

    def __unicode__(self): 
        return self.title 
		
    def save(self, force_insert=False, force_update=False): 
        self.body_html = markdown(self.body) 
        if self.excerpt: 
            self.excerpt_html = markdown(self.excerpt) 
        super(Post, self).save(force_insert, force_update)
		
    def get_absolute_url(self):  
        return "/post/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug )