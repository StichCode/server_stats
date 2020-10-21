from datetime import datetime


def get_body(fields: dict) -> str:

    return '\n'.join(
        ("\t{0:20}: {1}".format(descr, val) for descr, val in fields.items())
    )


def template_info(name_func: str, fields: dict = None, body: str = None) -> str:
    if body is None:
        body = get_body(fields)
    result = "\n{0}\t{1} ({2}) \n{3}\n{0}".format('= ' * 6, name_func, datetime.now(), body)
    return result