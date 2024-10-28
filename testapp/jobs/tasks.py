import time
from celery.canvas import chord
from celery.utils.log import get_task_logger

from testapp.celery import app


logger = get_task_logger(__name__)


# Celery chords
@app.task(bind=True)
def run_parent_task(self):
    logger.info("Parent task starting...")
    time.sleep(5)

    # 99 child tasks
    subtasks = []
    for i in range(1, 100):
        subtasks.append(run_child_task.s(i))
    
    logger.info("Parent task starting chord...")
    result = chord(subtasks)(callback.s())
    logger.info("Parent task complete!")


@app.task(bind=True)
def run_child_task(self, i):
    logger.info(f"Child task {i} starting...")
    time.sleep(3)
    logger.info(f"Child task {i} complete!")
    return i


@app.task(bind=True)
def callback(self, results):
    time.sleep(3)
    logger.info(f"Callback complete!")
