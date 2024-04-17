from typing import List,Union
from schemas.base import SummaryPayloadSchema
from models.text_summary_model import TextSummary

async def post(payload:SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url,summary="Dummy summary")
    await summary.save()
    return summary.id


