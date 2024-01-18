from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4,editable=True,primary_key=True)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)
    
    class Meta:
        abstract=True
        
class Todo(BaseModel):
    todo_name=models.CharField(max_length=100)
    is_completed=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="User_todos")
    
    def __str__(self) -> str:
        return "Todo "+str(self.uuid)
    
    
    
    
