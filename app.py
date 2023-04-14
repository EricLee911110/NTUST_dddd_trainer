import fire

from loguru import logger
from utils import project_manager
from utils import cache_data
from utils import train


class App:

    def __init__(self):
        logger.info("\nHello baby~")

    def create(self, project_name: str, single: bool = False):
        logger.info("\nCreate Project ----> {}".format(project_name))
        pm = project_manager.ProjectManager()
        pm.create_project(project_name, single)

    def cache(self, project_name: str, base_path: str, search_type: str = "name"):
        logger.info("\nCaching Data ----> {}\nPath ----> {}".format(project_name, base_path))
        cache = cache_data.CacheData(project_name)
        cache.cache(base_path, search_type)
        pass

    def train(self, project_name: str):
        for ModelVersion in range(1):
            logger.info("\nStart Train ----> {}\n".format(project_name))
            trainer = train.Train(project_name)
            # 1. pass in version variable
            ModelVersion = 0
            trainer.start(ModelVersion) 
            # delete checkpoints directory

            # append checkpoints directory



if __name__ == '__main__':
    fire.Fire(App)
