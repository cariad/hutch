from hutch.request import Request


def handle(request: Request) -> None:
    """
    Handle a request to take an action on a website.

    Args:
        request: Request.
    """

    print(f"TODO: Perform '{request.verb}' on '{request.domain}'.")
