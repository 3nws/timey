from typing import Dict, Any

Response = Dict[str, Any]


class CalculationResult:

    __slots__ = (
        "payload",
        "year",
        "month",
        "day",
        "hour",
        "minute",
        "seconds",
        "milliseconds",
        "date_time",
        "date",
        "time",
        "dst_active",
    )

    def __init__(self, payload: Response) -> None:
        if payload:
            self.payload = payload
            self.year: int = payload.get("year", None)
            self.month: int = payload.get("month", None)
            self.day: int = payload.get("day", None)
            self.hour: int = payload.get("hour", None)
            self.minute: int = payload.get("minute", None)
            self.seconds: int = payload.get("seconds", None)
            self.milliseconds: int = payload.get("milliseconds", None)
            self.date_time: str = payload.get("date_time", None)
            self.date: str = payload.get("date", None)
            self.time: str = payload.get("time", None)
            self.dst_active: bool = payload.get("dstActive", None)

    def json(self) -> Response:
        return self.payload


class Calculation:

    __slots__ = (
        "payload",
        "time_zone",
        "original_date_time",
        "used_time_span",
        "calculation_result",
    )

    def __init__(self, payload: Response) -> None:
        if payload:
            self.payload = payload
            self.time_zone: str = payload.get("timeZone", None)
            self.original_date_time: str = payload.get("originalDateTime", None)
            self.used_time_span: str = payload.get("usedTimeSpan", None)
            self.calculation_result: CalculationResult = CalculationResult(
                payload.get("calculationResult", None)
            )

    def json(self) -> Response:
        return self.payload


class ConversionResult(CalculationResult):

    __slots__ = (
        "payload",
        "time_zone",
    )

    def __init__(self, payload: Response) -> None:
        super().__init__(payload)
        if payload:
            self.payload = payload
            self.time_zone: str = payload.get("time_zone", None)

    def json(self) -> Response:
        return self.payload


class Conversion:

    __slots__ = (
        "payload",
        "from_time_zone",
        "from_date_time",
        "to_time_zone",
        "conversion_result",
    )

    def __init__(self, payload: Response) -> None:
        if payload:
            self.payload = payload
            self.from_time_zone: str = payload.get("fromTimeZone", None)
            self.from_date_time: str = payload.get("fromDateTime", None)
            self.to_time_zone: str = payload.get("toTimezone", None)
            self.conversion_result: ConversionResult = ConversionResult(
                payload.get("conversionResult", None)
            )

    def json(self) -> Response:
        return self.payload


class CurrentTime(ConversionResult):

    __slots__ = ("payload", "day_of_week")

    def __init__(self, payload: Response) -> None:
        super().__init__(payload)
        if payload:
            self.payload = payload
            self.day_of_week: str = payload.get("dayOfWeek", None)

    def json(self) -> Response:
        return self.payload


class DayOfTheWeekResult:

    __slots__ = ("payload", "day_of_week")

    def __init__(self, payload: Response) -> None:
        if payload:
            self.payload = payload
            self.day_of_week: str = payload.get("dayOfWeek", None)

    def json(self) -> Response:
        return self.payload


class Duration:

    __slots__ = (
        "payload",
        "days",
        "nanosecond_of_day",
        "hours",
        "minutes",
        "seconds",
        "milliseconds",
        "subsecond_ticks",
        "subsecond_nanoseconds",
        "bcl_compatible_ticks",
        "total_days",
        "total_hours",
        "total_minutes",
        "total_seconds",
        "total_milliseconds",
        "total_ticks",
        "total_nanoseconds",
    )

    def __init__(self, payload: Response) -> None:
        if payload:
            self.payload = payload
            self.days: int = payload.get("days", None)
            self.nanosecond_of_day: int = payload.get("nanosecondOfDay", None)
            self.hours: int = payload.get("hours", None)
            self.minutes: int = payload.get("minutes", None)
            self.seconds: int = payload.get("seconds", None)
            self.milliseconds: int = payload.get("milliseconds", None)
            self.subsecond_ticks: int = payload.get("subsecondTicks", None)
            self.subsecond_nanoseconds: int = payload.get("subsecondNanoseconds", None)
            self.bcl_compatible_ticks: int = payload.get("bclCompatibleTicks", None)
            self.total_days: int = payload.get("totalDays", None)
            self.total_hours: int = payload.get("totalHours", None)
            self.total_minutes: int = payload.get("totalMinutes", None)
            self.total_seconds: int = payload.get("totalSeconds", None)
            self.total_milliseconds: int = payload.get("totalMilliseconds", None)
            self.total_ticks: int = payload.get("totalTicks", None)
            self.total_nanoseconds: int = payload.get("totalNanoseconds", None)

    def json(self) -> Response:
        return self.payload


class Offset:

    __slots__ = ("payload", "seconds", "milliseconds", "ticks", "nanoseconds")

    def __init__(self, payload: Response) -> None:
        if payload:
            self.payload = payload
            self.seconds: int = payload.get("seconds", None)
            self.milliseconds: int = payload.get("milliseconds", None)
            self.ticks: int = payload.get("ticks", None)
            self.nanoseconds: int = payload.get("nanoseconds", None)

    def json(self) -> Response:
        return self.payload


class DstInterval:

    __slots__ = (
        "payload",
        "dst_name",
        "dst_offset_to_utc",
        "dst_offset_to_standard_time",
        "dst_start",
        "dst_end",
        "dst_duration",
    )

    def __init__(self, payload: Response) -> None:
        if payload:
            self.payload = payload
            self.dst_name: str = payload.get("dstName", None)
            self.dst_offset_to_utc: Offset = Offset(payload.get("dstOffsetToUtc", None))
            self.dst_offset_to_standard_time: Offset = Offset(
                payload.get("dstOffsetToStandardTime", None)
            )
            self.dst_start: str = payload.get("dstStart", None)
            self.dst_end: str = payload.get("dstEnd", None)
            self.dst_duration: Duration = Duration(payload.get("dstDuration", None))

    def json(self) -> Response:
        return self.payload


class TimeZoneData:

    __slots__ = (
        "payload",
        "time_zone",
        "current_local_time",
        "current_utc_offset",
        "standard_utc_offset",
        "has_day_light_saving",
        "is_day_light_saving_active",
        "dst_interval",
    )

    def __init__(self, payload: Response) -> None:
        if payload:
            self.payload = payload
            self.time_zone: str = payload.get("timeZone", None)
            self.current_local_time: str = payload.get("currentLocalTime", None)
            self.current_utc_offset: Offset = Offset(
                payload.get("currentUtcOffset", None)
            )
            self.standard_utc_offset: Offset = Offset(
                payload.get("standardUtcOffset", None)
            )
            self.has_day_light_saving: bool = payload.get("hasDayLightSaving", None)
            self.is_day_light_saving_active: bool = payload.get(
                "isDayLightSavingActive", None
            )
            self.dst_interval: DstInterval = DstInterval(
                payload.get("dstInterval", None)
            )

    def json(self) -> Response:
        return self.payload


class Translation:

    __slots__ = (
        "payload",
        "date_time",
        "language_code",
        "friendly_date_time",
        "friendly_date",
        "friendly_time",
    )

    def __init__(self, payload: Response) -> None:
        if payload:
            self.payload = payload
            self.date_time: str = payload.get("dateTime", None)
            self.language_code: str = payload.get("languageCode", None)
            self.friendly_date_time: str = payload.get("friendlyDateTime", None)
            self.friendly_date: str = payload.get("friendlyDate", None)
            self.friendly_time: str = payload.get("friendlyTime", None)

    def json(self) -> Response:
        return self.payload
