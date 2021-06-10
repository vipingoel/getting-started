from typing import NewType

UserId = NewType('UserId', int)


def get_user_name(user_id: UserId) -> str:
    print(user_id)
    print(type(user_id))


get_user_name(312)
get_user_name(UserId(312))
