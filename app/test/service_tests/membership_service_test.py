from app.main.services.membership_service import MembershipService
from app.main.dto.membership_dto import MembershipDTO

class TestMembershipService:

    def test_add_single_membership(self):

        # Assert
        service = MembershipService()

        # Act
        result = service.add_membership(MembershipDTO(id=1, name='Jack Sparrow', level='Singleton'))
        stored_membership = service.get_membership(1)

        # Assert
        assert result
        assert stored_membership.id == 1
        assert stored_membership.name == 'Jack Sparrow'
        assert stored_membership.level == 'Singleton'

    def test_add_duplicated_membership(self):

        # Assert
        service = MembershipService()

        # Act
        membership_one_added = service.add_membership(MembershipDTO(id=1, name='Jack Sparrow', level='Singleton'))
        membership_two_added = service.add_membership(MembershipDTO(id=1, name='Jon Snow', level='Code Geek'))

        # Arrange
        assert membership_one_added
        assert not membership_two_added
