from fastapi import HTTPException


class LocalMartException(HTTPException):
    """
    Base exception for LocalMart.
    """

    def __init__(
        self,
        status_code: int,
        message: str,
    ):
        super().__init__(
            status_code=status_code,
            detail=message,
        )
