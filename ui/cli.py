from argparse import _SubParsersAction, ArgumentParser, Namespace


def init(program_name, commands: dict[str, dict[str, dict]]) -> ArgumentParser:
    parser: ArgumentParser = ArgumentParser(prog=program_name)
    subparser: _SubParsersAction = parser.add_subparsers(dest="command", required=True)
    build_parsers(subparser, commands)

    return parser


def args(parser: ArgumentParser) -> Namespace:
    args: Namespace = parser.parse_args()
    print(f"Working with: {args}")
    return args


def build_parsers(subparser: _SubParsersAction, commands: dict[str, dict[str, dict]]):
    for c, cfg in commands.items():
        command = subparser.add_parser(c)
        for a, acfg in cfg.items():
            kwargs = build_kwargs(acfg)
            command.add_argument(a, **kwargs)


def build_kwargs(cfg: dict) -> dict:
    kwargs = {}
    for a in cfg:
        kwargs[a] = cfg[a]

    return kwargs
