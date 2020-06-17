from dataclasses import dataclass, asdict

@dataclass
class MembershipDTO:

    id: int
    name: str
    level: str

    def to_dict(self):
        return asdict(self)
