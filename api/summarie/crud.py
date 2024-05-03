from typing import List, Union

from fastapi.exceptions import HTTPException

from models.text_summary_model import TextSummary
from schemas.base import SummaryPayloadSchema


#! get_all
async def get_all() -> List:
    """
    Retrieve all text summaries.

    Returns:
    - summaries (List): A list of all text summaries.

    This function asynchronously retrieves all text summaries from the database. It uses the `all()` method of the `TextSummary` model to fetch all records from the corresponding table. The `values()` method is used to retrieve the values of all fields in each record.

    The function returns a list containing all the retrieved text summaries.
    """
    summaries = await TextSummary.all().values()
    return summaries


# !post
async def post(payload: SummaryPayloadSchema) -> TextSummary:
    """
    Creates a summary based on the provided payload and returns the summary ID.

    Args:
        payload (SummaryPayloadSchema): The payload containing information for creating the summary. => url

    Returns:
        int: The ID of the created summary.
    """
    summarie = TextSummary(url=payload.url, summary="Dummy summary")
    await summarie.save()
    return summarie


#! get
async def get(id: int) -> Union[dict, None]:
    """
    Retrieve a text summary by its ID.

    Args:
        id (int): The ID of the text summary to retrieve.

    Returns:
        Union[dict, None]: A dictionary containing the summary data if found, or None if not found.
    """
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


# !delete
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
