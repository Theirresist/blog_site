from django.db import models



class Category(models.Model):
    name = models.CharField(max_length = 30, help_text = 'Выберите категорию для статьи')
  
    def __str__(self):
        return self.name



class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    second_name = models.CharField(max_length = 30)
    date_of_birth = models.DateField(null = True, blank = True)
    name = str(first_name) + '' + str(second_name)

    def display_category(self):
        return ', '.join([ category.name for category in self.category.all()[:3] ])
    
    display_category.short_description = 'Категория'


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('author-detail', args = [str(self.id)]) 



class Article(models.Model):
    title = models.CharField(max_length = 150)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    item = models.TextField('max_length = 10000', help_text="Введите текст")
    

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
    

    def __str__(self):
        return self.title




