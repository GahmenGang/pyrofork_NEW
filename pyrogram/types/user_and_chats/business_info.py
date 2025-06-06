#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

from typing import Optional, Dict

from pyrogram import types, raw
from ..object import Object


class BusinessInfo(Object):
    """Business information of a user.

    Parameters:
        address (``str``, *optional*):
            Address of the business.

        location (:obj:`~pyrogram.types.Location`, *optional*):
            Location of the business on the map.

        greeting_message (:obj:`~pyrogram.types.BusinessMessage`, *optional*):
            Greeting message of the business.

        away_message (:obj:`~pyrogram.types.BusinessMessage`, *optional*):
            Away message of the business.

        working_hours (:obj:`~pyrogram.types.BusinessWorkingHours`, *optional*):
            Working hours of the business.
    """

    def __init__(
        self,
        *,
        address: str = None,
        location: "types.Location" = None,
        greeting_message: "types.BusinessMessage" = None,
        away_message: "types.BusinessMessage" = None,
        working_hours: "types.BusinessWorkingHours" = None,

    ):
        self.address = address
        self.location = location
        self.greeting_message = greeting_message
        self.away_message = away_message
        self.working_hours = working_hours

    @staticmethod
    def _parse(
        client,
        user: "raw.types.UserFull" = None,
        users: Dict[int, "raw.types.User"] = None
    ) -> Optional["BusinessInfo"]:
        working_hours = getattr(user, "business_work_hours", None)
        location = getattr(user, "business_location", None)
        greeting_message = getattr(user, "business_greeting_message", None)
        away_message = getattr(user, "business_away_message", None)

        if not any((working_hours, location, greeting_message, away_message)):
            return None

        return BusinessInfo(
            address=getattr(location, "address", None),
            location=types.Location._parse(client, getattr(location, "geo_point", None)),
            greeting_message=types.BusinessMessage._parse(client, greeting_message, users),
            away_message=types.BusinessMessage._parse(client, away_message, users),
            working_hours=types.BusinessWorkingHours._parse(working_hours),
        )
