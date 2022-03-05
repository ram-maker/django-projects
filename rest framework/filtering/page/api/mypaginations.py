from rest_framework.pagination import PageNumberPagination
class MyPageNumberPagination(PageNumberPagination):
    page_size=4
    page_query_param='p'#for overriding default name 'page' to p
    page_size_query_param='records'#defines how many records to be used in particular page