from fastapi import APIRouter,HTTPException
from schemas.base import SummaryPayloadSchema,SummaryResponseSchema
from .crud import post_summarie,delete_summaries

# Create a router object for handling routes related to summaries
router = APIRouter(tags=["Summaries"])

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
    summary_id = await post_summarie(payload)
    summarie_object = {
        "id": summary_id,
        "url": payload.url
    }
    return summarie_object

@router.delete("/",status_code=202)
async def clear_summaries() -> object:
    """
    Clear all summaries by deleting them from the database.

    Returns:
        object: A dictionary containing a success message.

    """
    message = await delete_summaries()
    return message