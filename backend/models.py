from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

class create_mixin:
    created_on: datetime
    created_by: str

class update_mixin:
    updated_on: Optional[datetime]
    updated_by: Optional[str]

class delete_mixin:
    deleted_on: Optional[datetime]
    deleted_by: Optional[str]

class create_update_model(create_mixin, update_mixin):
    pass    
    
class create_update_delete_model(create_mixin, update_mixin, delete_mixin):
    pass
    
@dataclass
class User(create_update_delete_model):
    id: int
    email: str

@dataclass
class Skill(create_update_delete_model):
    id: int
    name: str

@dataclass
class Company(create_update_delete_model):
    id: int
    name: str
    description: str

@dataclass
class Job(create_update_delete_model):
    id: int
    name: str
    description: str
    requirements: List[str]
    benefits: List[str]
    skills: List[str]
    company: Company
    recruiter: User