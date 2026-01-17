from argparse import Namespace
from typing import Any

from ytworker.core import services


def run_command(args: Namespace) -> str:
    kwargs = args._get_kwargs()

    command = kwargs[0][1]
    gen_kwargs = generate_kwargs(kwargs[1:])
    return services.run_command(command, **gen_kwargs)
    

def generate_kwargs(args: list[tuple[str, Any]]) -> dict[str, Any]:
    kwargs = {}
    for a in args:
        kwargs[a[0]] = a[1]
    return kwargs