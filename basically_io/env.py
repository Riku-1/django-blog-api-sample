import environ

env = environ.Env()
env.read_env('.env')


def get_env(key: str):
    return env(key)
