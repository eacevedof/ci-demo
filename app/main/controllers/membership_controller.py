from flask import Blueprint, jsonify, request
from injector import inject

from ..services.membership_service import MembershipService
from ..dto.membership_dto import MembershipDTO

blueprint = Blueprint('membership', __name__, url_prefix="/memberships")

@blueprint.route('', methods=('GET',))
@inject
def get(membership_service: MembershipService):

    memberships = membership_service.get_memberships()

    response = [membership.to_dict() for membership in memberships]
    return jsonify(response)

@blueprint.route('', methods=('POST',))
def post(membership_service: MembershipService):
    request_data = request.json
    dto = MembershipDTO(id=request_data.get('id'),
                        name=request_data.get('name'),
                        level=request_data.get('level'))

    add_result = membership_service.add_membership(dto)
    status_code = 201 if add_result else 409

    return jsonify(sucess=add_result), status_code
