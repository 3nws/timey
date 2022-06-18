import asyncio
import json
import aiohttp

from typing import (
    Optional,
    Any,
    List,
    Dict,
    Union,
)

from aiohttp import ClientSession

from .exceptions import *
from .models import *


class Endpoints:
    base = "https://www.timeapi.io/api"
    time = f"{base}/Time/current"
    timezone = f"{base}/TimeZone"
    conversion = f"{base}/Conversion"
    calc = f"{base}/Calculation"


class http:

    _session: ClientSession

    def __init__(self) -> None:
        self.loop: asyncio.AbstractEventLoop
        self.background_tasks = set()
        self.header = {"Content-Type": "application/json"}

    def __await__(self):
        return self.start().__await__()

    async def start(self):
        loop = asyncio.get_running_loop()
        self.loop = loop
        self._session = aiohttp.ClientSession()
        return self

    async def _make_req(
        self, url: str, method: str, data: Optional[Dict[str, Any]] = None
    ) -> Response:
        if method == "GET":
            async with self._session.get(url) as res:
                if res.status == 200:
                    resp = await res.read()
                    return json.loads(resp)
                raise APIError()
        elif data is not None:
            async with self._session.post(url, json=data, headers=self.header) as res:
                if res.status == 200:
                    resp = await res.read()
                    return json.loads(resp)
                raise APIError()
        else:
            raise MissingRequestBody()

    async def _get_current_time_by_name(self, time_zone: str) -> CurrentTime:
        url = f"{Endpoints.time}/zone?timeZone={time_zone}"
        return CurrentTime(await self._make_req(url, "GET"))

    async def _get_current_time_by_geo(
        self, latitude: float, longitude: float
    ) -> CurrentTime:
        url = f"{Endpoints.time}/coordinate?latitude={latitude}&longitude={longitude}"
        return CurrentTime(await self._make_req(url, "GET"))

    async def _get_current_time_by_ip(self, ip: str) -> CurrentTime:
        url = f"{Endpoints.time}/ip?ipAddress={ip}"
        return CurrentTime(await self._make_req(url, "GET"))

    async def _get_available_timezones(self) -> List[str]:
        url = f"{Endpoints.timezone}/AvailableTimeZones"
        return await self._make_req(url, "GET")  # type: ignore

    async def _get_timezone_by_name(self, time_zone: str) -> TimeZoneData:
        url = f"{Endpoints.timezone}/zone?timezone={time_zone}"
        return TimeZoneData(await self._make_req(url, "GET"))

    async def _get_timezone_by_geo(
        self, latitude: float, longitude: float
    ) -> TimeZoneData:
        url = (
            f"{Endpoints.timezone}/coordinate?latitude={latitude}&longitude={longitude}"
        )
        return TimeZoneData(await self._make_req(url, "GET"))

    async def _get_timezone_by_ip(self, ip: str) -> TimeZoneData:
        url = f"{Endpoints.timezone}/ip?ipAddress={ip}"
        return TimeZoneData(await self._make_req(url, "GET"))

    async def _convert_time(self, data: Dict[str, Any]) -> Conversion:
        url = f"{Endpoints.conversion}/ConvertTimeZone"
        return Conversion(await self._make_req(url, "POST", data=data))

    async def _get_user_friendly(self, data: Dict[str, Any]) -> Translation:
        url = f"{Endpoints.conversion}/Translate"
        return Translation(await self._make_req(url, "POST", data=data))

    async def _get_dotw(self, date: str) -> DayOfTheWeekResult:
        url = f"{Endpoints.conversion}/DayOfTheWeek/{date}"
        return DayOfTheWeekResult(await self._make_req(url, "GET"))

    async def _get_doty(self, date: str) -> Response:
        url = f"{Endpoints.conversion}/DayOfTheYear/{date}"
        return await self._make_req(url, "GET")

    async def _add_time(self, data: Dict[str, Any]) -> Calculation:
        url = f"{Endpoints.calc}/current/increment"
        return Calculation(await self._make_req(url, "POST", data=data))

    async def _subtract_time(self, data: Dict[str, Any]) -> Calculation:
        url = f"{Endpoints.calc}/current/decrement"
        return Calculation(await self._make_req(url, "POST", data=data))

    async def _add_time_to_custom(self, data: Dict[str, Any]) -> Calculation:
        url = f"{Endpoints.calc}/custom/increment"
        return Calculation(await self._make_req(url, "POST", data=data))

    async def _subtract_time_from_custom(self, data: Dict[str, Any]) -> Calculation:
        url = f"{Endpoints.calc}/custom/decrement"
        return Calculation(await self._make_req(url, "POST", data=data))
