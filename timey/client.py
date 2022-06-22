from typing import Any, Coroutine, Optional, List
from typing_extensions import Self

from .http import http, Response
from .models import *


class Timey:
    async def __aenter__(self):
        return await self.start()

    async def __aexit__(self, exc_type, exc, tb):
        await self.http.end()

    async def start(self) -> Self:
        self.http = await http().start()
        return self

    async def get_current_by_name(self, time_zone: str) -> CurrentTime:
        return await self.http._get_current_time_by_name(time_zone)

    async def get_current_by_geo(
        self, latitude: float, longitude: float
    ) -> CurrentTime:
        return await self.http._get_current_time_by_geo(latitude, longitude)

    async def get_current_by_ip(self, ip: str) -> CurrentTime:
        return await self.http._get_current_time_by_ip(ip)

    async def get_available_timezones(self) -> List[str]:
        return await self.http._get_available_timezones()

    async def get_timezone_by_name(self, time_zone: str) -> TimeZoneData:
        return await self.http._get_timezone_by_name(time_zone)

    async def get_timezone_by_geo(
        self, latitude: float, longitude: float
    ) -> TimeZoneData:
        return await self.http._get_timezone_by_geo(latitude, longitude)

    async def get_timezone_by_ip(self, ip: str) -> TimeZoneData:
        return await self.http._get_timezone_by_ip(ip)

    async def convert_time(
        self, src: str, time: str, to: str, dst_ambiguity: Optional[str] = ""
    ) -> Conversion:
        return await self.http._convert_time(
            data={
                "fromTimeZone": src,
                "dateTime": time,
                "toTimezone": to,
                "dstAmbiguity": dst_ambiguity,
            }
        )

    async def get_user_friendly(self, time: str, lang: str) -> Translation:
        return await self.http._get_user_friendly(
            data={
                "dateTime": time,
                "languageCode": lang,
            }
        )

    async def day_of_the_week(self, date: str) -> DayOfTheWeekResult:
        return await self.http._get_dotw(date)

    async def day_of_the_year(self, date: str) -> Response:
        return await self.http._get_doty(date)

    async def add_time(self, time_zone: str, time_span: str) -> Calculation:
        return await self.http._add_time(
            data={
                "timeZone": time_zone,
                "timeSpan": time_span,
            }
        )

    async def subtract_time(self, time_zone: str, time_span: str) -> Calculation:
        return await self.http._subtract_time(
            data={
                "timeZone": time_zone,
                "timeSpan": time_span,
            }
        )

    async def add_time_to_custom(
        self,
        time_zone: str,
        time: str,
        time_span: str,
        dst_ambiguity: Optional[str] = "",
    ) -> Calculation:
        return await self.http._add_time_to_custom(
            data={
                "timeZone": time_zone,
                "dateTime": time,
                "timeSpan": time_span,
                "dstAmbiguity": dst_ambiguity,
            }
        )

    async def subtract_time_from_custom(
        self,
        time_zone: str,
        time: str,
        time_span: str,
        dst_ambiguity: Optional[str] = "",
    ) -> Calculation:
        return await self.http._subtract_time_from_custom(
            data={
                "timeZone": time_zone,
                "dateTime": time,
                "timeSpan": time_span,
                "dstAmbiguity": dst_ambiguity,
            }
        )
