from ytworker.config import COMMANDS_CONFIGURATION, PROGRAM_NAME
import ytworker.ui.cli as cli
import ytworker.core.command_handler as command_handler


if __name__ == "__main__":
    parser = cli.init(PROGRAM_NAME, COMMANDS_CONFIGURATION)
    args = cli.extract_args(parser)
    
    report: str = command_handler.run_command(args)
    print(report)