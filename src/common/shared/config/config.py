from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from dotenv import load_dotenv

load_dotenv()


class AuthConfig(BaseSettings):
    EXPIRES_AT: int
    SECRET_KEY: SecretStr

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
    Auth: AuthConfig = AuthConfig()
    Database: DatabaseConfig = DatabaseConfig()
    Redis: RedisConfig = RedisConfig()
    Kafka: KafkaConfig = KafkaConfig()

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


settings: Settings = Settings()
