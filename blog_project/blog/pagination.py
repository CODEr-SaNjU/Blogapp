from rest_framework import  pagination

class TeacherPagination(pagination.PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'  # Optional: query parameter to override `PAGE_SIZE`
    max_page_size = 100  # Optional: maximum number of items per page