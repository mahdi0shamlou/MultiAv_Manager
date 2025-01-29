from fastapi import FastAPI
from tasks import router_tasks

app = FastAPI()
app.title="MultiAv Manager"
app.include_router(router_tasks)


# Check if the script is run directly and start the server
if __name__ == "__main__":
    import uvicorn
    import configparser
    import os
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'server.ini')
    # Read configuration from server.ini
    config = configparser.ConfigParser()
    config.read(config_path)

    print("Config path:", config_path)
    print(config.sections())

    # Extract settings
    host = config['server']['host']
    port = int(config['server']['port'])
    log_level = config['server']['log_level']

    uvicorn.run(app, host=host, port=port, log_level=log_level)