from fastapi import APIRouter,HTTPException
from schemas.base import SummaryPayloadSchema,SummaryResponseSchema
from .crud import post

router = APIRouter(tags=["Summaries"])

@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema):
    summary_id = await post(payload)
    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    return response_object