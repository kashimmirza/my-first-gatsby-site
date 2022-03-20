from backend.api.viewsets import PersonViewSet, StudentViewSet, FacultyViewSet, ReadingMaterialViewSet, FaceViewSet, DepartmentViewSet, CourseViewSet, SectionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('persons', PersonViewSet)
router.register('students', StudentViewSet)
router.register('facultys', FacultyViewSet)
router.register('readingmaterials', ReadingMaterialViewSet)
router.register('faces', FaceViewSet)
router.register('departments', DepartmentViewSet)
router.register('courses', CourseViewSet)
router.register('sections', SectionViewSet)
