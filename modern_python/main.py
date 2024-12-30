from .settings import Settings

if __name__ == "__main__":
    env = Settings()
    print(f"api_key: {env.api_key}")
    print(f"auth_key: {env.auth_key}")
