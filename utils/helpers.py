import socket


def internet_available():

    try:

        socket.create_connection(
            ("huggingface.co", 443),
            timeout=5
        )

        return True

    except Exception:

        return False