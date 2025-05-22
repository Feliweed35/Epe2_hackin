from django.urls import path
from .views.viewTest import TestView
from .views.viewDeepseek import DeepSeekView
from .views.viewSemanticAnalysis import SemanticAnalysisView

urlpatterns = [
    path('test/', TestView.as_view(), name='test-endpoint'),
    path('deepseek/', DeepSeekView.as_view(), name='deepseek-endpoint'),
    path('semantic-analysis/', SemanticAnalysisView.as_view(), name='semantic-analysis-endpoint'),
]
