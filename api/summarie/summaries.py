from typing import List

from fastapi import APIRouter, HTTPException

from schemas.base import (
    SummaryGetResponseSchema,
    SummaryPayloadSchema,
    SummaryResponseSchema,
)

from .crud import delete_summaries, get, get_all, post

# Create a router object for handling routes related to summaries
router = APIRouter(tags=["Summaries"])


#! read_all_summaries
@router.get("/", response_model=List[SummaryResponseSchema])
async def read_all_summaries() -> List[SummaryResponseSchema]:
    """
    Retrieve all summaries.

    Returns:
    - summaries (List[SummaryResponseSchema]): A list of all summaries.

    This function is an API endpoint that retrieves all summaries by calling the `get_all()` function asynchronously. The `response_model` decorator ensures that the response data is automatically validated against the `SummaryResponseSchema` model.

    The function returns a list of all retrieved summaries, with each summary represented by the `SummaryResponseSchema` model.
    """
    return await get_all()


#! create_summary
@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema):
    """
    Creates a summary based on the provided payload.

    Args:
        payload (SummaryPayloadSchema): The payload containing information for creating the summary => url

    Returns:
        dict: The summary object with keys "id" and "url".
    """
    summarie = await post(payload)
    summarie_object = {
        "id": summarie.id,
        "url": payload.url,
        "summary": summarie.summary,
        "created_at": summarie.created_at,
    }
    return summarie_object


#! read_summary
@router.get("/{id}/", response_model=SummaryGetResponseSchema)
async def read_summary(id: int) -> dict:
    """
    Retrieve a summary by its ID.

    Parameters:
    - id (int): The ID of the summary to retrieve.

    Returns:
    - dict: The retrieved summary as a dictionary.

    Raises:
    - HTTPException: If the summary is not found, a 404 status code with a "Summary not found" detail will be raised.
    """
    summary = await get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary


#! clear_summaries
@router.delete("/", status_code=202)
async def clear_summaries() -> object:
    """
    Clear all summaries by deleting them from the database.

    Returns:
        object: A dictionary containing a success message.
    """
    message = await delete_summaries()
    return message
