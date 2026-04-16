from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ListSessionsQuery:
    user_id: Optional[str] = None