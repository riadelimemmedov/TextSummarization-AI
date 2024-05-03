from datetime import datetime
from typing import Optional

from pydantic import AnyHttpUrl, BaseModel, Field


#! SummaryPayloadSchema
class SummaryPayloadSchema(BaseModel):
    """
    Schema for a summary payload.

    Attributes:
    - url (AnyHttpUrl): The URL of the summary.
    """

    url: AnyHttpUrl


#! SummaryGetResponseSchema
class SummaryGetResponseSchema(BaseModel):
    """
    Schema for a summary response.

    Attributes:
    - id (int): The ID of the summary.
    - summary (str): The text content of the summary.
    - created_at (datetime): The timestamp indicating when the summary was created. If not provided, it defaults to the current datetime.
    """

    id: int
    summary: str
    created_at: datetime = Field(default_factory=datetime.now)


#! SummaryResponseSchema
class SummaryResponseSchema(SummaryPayloadSchema, SummaryGetResponseSchema):
    """
    Schema for a summary response.

    Inherits:
    - SummaryPayloadSchema: Schema for the payload of a summary.
    - SummaryGetResponseSchema: Schema for the response of a summary.

    This class combines the attributes from both the SummaryPayloadSchema and SummaryGetResponseSchema classes.
    """

    pass


# !SummaryUpdatePayloadSchema
class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    """
    Schema for updating a summary payload.

    Inherits:
    - SummaryPayloadSchema: Schema for the payload of a summary.

    Additional Attribute:
    - summary (str): The updated summary text.
    """

    summary: str
