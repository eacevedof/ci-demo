from app.main.services.membership_service import MembershipService
from app.main.dto.membership_dto import MembershipDTO

class TestMembershipService:

    def test_add_single_membership(self):

        # Assert
        service = MembershipService()

        # Act
        result = service.add_membership(MembershipDTO(id=1, name='Jack Sparrow', level='Singleton'))

        # Arrange
        assert result

    def test_add_duplicated_membership(self):

        # Assert
        service = MembershipService()

        # Act
        membership_one_added = service.add_membership(MembershipDTO(id=1, name='Jack Sparrow', level='Singleton'))
        membership_two_added = service.add_membership(MembershipDTO(id=1, name='Jon Snow', level='Code Geek'))

        # Arrange
        assert membership_one_added
        assert not membership_two_added
