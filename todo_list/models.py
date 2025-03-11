from django.db import models
from django.urls import reverse
# Create your models here.


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
class ToDoItem(models.Model):
    title= models.CharField(max_length=250)
    description = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date =models.DateTimeField(auto_now=True,null=True, blank=True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title}: due {self.due_date}"
    
    def get_absolute_url(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])    
    
    def get_context_data(self): 
        context = super().get_context_data() 
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"]) 
        return context
    
    class Meta:
        ordering =["due_date"]
    