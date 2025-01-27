
class ClientDeprecationWarning(DeprecationWarning):
    """Warning for deprecated client features."""
    pass


class ClientPendingDeprecationWarning(PendingDeprecationWarning):
    pass


class ClientExperimentalWarning(UserWarning):
    pass
