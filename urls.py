from datetime import date
import views as view


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': view.Index(),
    '/about/': view.About(),
    '/contacts/': view.Contacts(),
    '/study_programs/': view.StudyPrograms(),
    '/courses-list/': view.CoursesList(),
    '/create-course/': view.CreateCourse(),
    '/create-category/': view.CreateCategory(),
    '/category-list/': view.CategoryList(),
    '/copy-course/': view.CopyCourse(),
}
