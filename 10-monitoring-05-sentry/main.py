import sentry_sdk

sentry_sdk.init(
    dsn="https://3cd55e44dff73320a482ccae6e6d5022@o4510265587859456.ingest.de.sentry.io/4510267145846864",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    environment ="development",
    release= "1.0"
)

if __name__ == "__main__":
    division_zero = 1/0