from fastapi import Request
import time
import logging


# Configuration logging for middlewares and set status to INFO for showing debug information
logging.basicConfig(level = logging.INFO)
log = logging.getLogger("middleware")



#! metric_middleware
async def metric_middleware(request: Request,call_next):
    """
    Middleware for measuring and logging the processing time of a request.

    This middleware calculates the processing time of a request by measuring the time taken between the beginning and
    the end of the request processing. It logs the total time in seconds at the INFO level using the logging module.

    Args:
        request (Request): The incoming request object.
        call_next (Callable): The callable representing the next middleware or the route handler.

    Returns:
        Any: The response returned by the next middleware or the route handler.

    Example:
        app.middleware('http')(metric_middleware)
    """
    # Get beginning stats
    start_time = time.perf_counter()
    
    # Process the request
    response = await call_next(request)
    
    # Get ending stats
    end_time = time.perf_counter()
    
    # Calculate stats
    total_time = end_time - start_time

    # Log the results
    logging.info(f" Total time: {(total_time):.2f}s")
    
    return response