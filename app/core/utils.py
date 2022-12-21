import re
from .schema import FieldError

INTEGRITY_ERROR_PATTERN = re.compile(r'\((.+)\)=\((.+)\)\s(.*)')


def parse_integrity_error(err_msgs: list[str]) -> list[FieldError]:
    errors = []
    for msg in err_msgs:
        result = re.search(pattern=INTEGRITY_ERROR_PATTERN, string=msg)
        field, value, error = result.groups()
        errors.append(FieldError(field=field, value=value, error=error))
    return errors
