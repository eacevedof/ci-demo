from ..dto.membership_dto import MembershipDTO


class MembershipService:

    def __init__(self):
        super().__init__()
        self.items = dict()

    def add_membership(self, new_membership: MembershipDTO) -> bool:

        result = False
        if new_membership.id not in self.items:
            self.items[new_membership.id] = new_membership
            result = True

        return result

    def get_memberships(self):
        return self.items.values()

    def get_membership(self, id) -> MembershipDTO:
        result = None
        if id in self.items:
            result = self.items[id]

        return result