from pydantic import BaseModel
from typing import Optional


class UserAccountContext(BaseModel):
    customer_id : int
    name: str
    tier: str = "basic" # premium, enterprise
    email: Optional[str] = None

class InputGuardRailOutput(BaseModel):
    is_off_topic: bool
    reason: str


class TechnicalOutputGuardRailOutput(BaseModel):
    contains_off_topic: bool
    contains_billing_data: bool
    contains_account_data: bool
    reason: str

# Handoff 시 로깅을 위한 데이터 모델
class HandoffData(BaseModel):
    to_agent_name: str
    issue_type: str
    issue_description: str
    reason: str