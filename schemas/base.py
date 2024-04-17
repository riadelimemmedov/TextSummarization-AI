from pydantic import AnyHttpUrl, BaseModel

#! SummaryPayloadSchema
class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl
    
    
#! SummaryResponseSchema
class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


# !SummaryUpdatePayloadSchema
class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str