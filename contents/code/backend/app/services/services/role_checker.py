# from fastapi import Depends, HTTPException, status

# from typing import Annotated

# from ..schemas.user import JWTUser
# from ..services.auth import validate_token

# from ..models import Role


# class RoleChecker:
#     def __init__(self, allowed_roles: list[Role]):
#         self.allowed_roles = allowed_roles

#     def __call__(self, user: Annotated[JWTUser, Depends(validate_token)]):
#         if user.get('role') in self.allowed_roles:
#             return True

#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="You do not have access to this resource"
#         )
