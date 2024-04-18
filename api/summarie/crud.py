from schemas.base import SummaryPayloadSchema
from models.text_summary_model import TextSummary
from fastapi.exceptions import HTTPException

# !post_summarie
async def post_summarie(payload:SummaryPayloadSchema) -> int:
    """
    Creates a summary based on the provided payload and returns the summary ID.

    Args:
        payload (SummaryPayloadSchema): The payload containing information for creating the summary. => url

    Returns:
        int: The ID of the created summary.
    """
    summary = TextSummary(url=payload.url,summary="Dummy summary")
    await summary.save()
    return summary.id

# !delete_summaries
async def delete_summaries() -> object:
    """
    Delete all summaries from the database.

    Returns:
        object: A dictionary containing a success message.

    Raises:
        HTTPException: If no summaries exist in the database.

    """
    notes = await TextSummary.all().delete()
    if not notes:
        raise HTTPException(
            status_code=400, detail="Your database model not exists summaries data"
        )
    return {"message": "All summaries deleted successfully"}
