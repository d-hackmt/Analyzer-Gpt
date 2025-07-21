from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from constants import WORK_DIR_DOCKER ,TIMEOUT_DOCKER


def getCommandLineExecutor():
    docker = DockerCommandLineCodeExecutor(
        work_dir= WORK_DIR_DOCKER , 
        timeout= TIMEOUT_DOCKER
    )
    return docker


async def start_docker_container(docker):
    print("Starting docker")
    await docker.start()
    print("docker started")
    
    

async def stop_docker_container(docker):
    print("Stoping docker")
    await docker.stop()
    print("docker stopped")
    