from celery import Celery
#for local rabbit
#app = Celery('tasks', broker='amqp://guest:guest@rabbit:5672/%2F')
#for container  rabbit
app = Celery('tasks', broker='amqp://guest:guest@172.17.0.1:5672/%2F')
@app.task
def add(x, y):
    return x + y