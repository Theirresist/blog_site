from django.db import models



class Genre(models.Model):
    name = models.CharField(max_length = 30, help_text = 'Выберите категорию для статьи')
  
    def __str__(self):
        return self.name



class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    date_of_birth = models.DateField(null = True, blank = True)
    

    

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse('author-detail', args = [str(self.id)]) 



class Article(models.Model):
    title = models.CharField(max_length = 150)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    item = models.TextField(max_length = 10000, help_text="Введите текст")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
    

    def __str__(self):
        return self.title




