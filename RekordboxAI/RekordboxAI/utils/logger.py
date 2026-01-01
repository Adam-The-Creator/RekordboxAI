class Logger:
    # ANSI color codes
    RESET = "\033[0m"
    BLUE = "\033[94m"     # INFO
    YELLOW = "\033[93m"   # WARNING
    RED = "\033[91m"      # ERROR

    @staticmethod
    def info(msg: str):
        print(f"{Logger.BLUE}[INFO] {msg}{Logger.RESET}")

    @staticmethod
    def warn(msg: str):
        print(f"{Logger.YELLOW}[WARNING] {msg}{Logger.RESET}")

    @staticmethod
    def error(msg: str):
        print(f"{Logger.RED}[ERROR] {msg}{Logger.RESET}")
