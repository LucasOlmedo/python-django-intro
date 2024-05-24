from books.api import viewsets as book_viewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', book_viewsets.BookViewSet)

urlpatterns = router.urls