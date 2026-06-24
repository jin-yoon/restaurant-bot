from pydantic import BaseModel


class UserAccountContext(BaseModel):
    name: str


class InputGuardRailOutput(BaseModel):
    is_off_topic: bool
    contains_bad_language: bool
    reason: str


class OuputGuardRailOutput(BaseModel):
    contains_off_topic: bool
    not_professional: bool
    leaks_internal_information: bool
    reason: str


class HandoffData(BaseModel):
    to_agent_name: str
    issue_type: str
    issue_description: str
    reason: str
