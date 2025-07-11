import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event('startup')
async def startup():
    logger.info('Server starting up')
    # original startup

@app.on_event('shutdown')
async def shutdown():
    logger.info('Server shutting down')
    # original shutdown

# For each endpoint, add try-except with logging
# Example:
#@app.get('/status')
#def get_status():
#    try:
#        status = # get status
#        logger.info('Status checked')
#        return status
#    except Exception as e:
#        logger.error(f'Status error: {e}')
#        raise 