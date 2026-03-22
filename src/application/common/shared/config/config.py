from dotenv import load_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class AppConfig(BaseSettings):
    TITLE: str

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


class AuthConfig(BaseSettings):
    EXPIRES_AT: int
    SECRET_KEY: SecretStr
    ALGORITHM: str

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


class DatabaseConfig(BaseSettings):
    POSTGRESQL_URL: SecretStr

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


class RedisConfig(BaseSettings):
    REDIS_URL: SecretStr

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


class KafkaConfig(BaseSettings):
    KAFKA_BOOTSTRAP_SERVER: SecretStr

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


class Settings(BaseSettings):
    App: AppConfig = AppConfig()
    Auth: AuthConfig = AuthConfig()
    Database: DatabaseConfig = DatabaseConfig()
    Redis: RedisConfig = RedisConfig()
    Kafka: KafkaConfig = KafkaConfig()

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


settings: Settings = Settings()
