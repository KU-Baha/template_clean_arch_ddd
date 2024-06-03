# from celery import Celery
#
# from application.config import settings
#
#
# def make_celery():
#     celery = Celery(
#         'my_project',
#         broker=settings.CELERY_BROKER_URL,
#         backend=settings.CELERY_RESULT_BACKEND,
#         include=['adapters.celery.tasks']
#     )
#
#     celery.conf.update(
#         result_expires=3600,
#     )
#
#     return celery
#
#
# celery_app = make_celery()
