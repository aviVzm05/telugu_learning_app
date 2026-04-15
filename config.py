"""
Configuration management for Telugu Learning App
Handles environment variables and app settings
"""
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration"""
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    PORT = int(os.getenv("PORT", 5050))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Session
    SESSION_TYPE = os.getenv("SESSION_TYPE", "filesystem")
    SESSION_PERMANENT = os.getenv("SESSION_PERMANENT", "False").lower() == "true"
    PERMANENT_SESSION_LIFETIME = int(os.getenv("PERMANENT_SESSION_LIFETIME", 3600))

    # TTS
    TTS_VOICE = os.getenv("TTS_VOICE", "te-IN")
    TTS_RATE = int(os.getenv("TTS_RATE", 180))
    TTS_VOLUME = float(os.getenv("TTS_VOLUME", 0.9))

    # Cache
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 300


class DevelopmentConfig(Config):
    """Development-specific configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production-specific configuration"""
    DEBUG = False
    LOG_LEVEL = "WARNING"


class TestingConfig(Config):
    """Testing-specific configuration"""
    TESTING = True
    DEBUG = True


# Select configuration based on environment
ENV = os.getenv("FLASK_ENV", "development").lower()
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
ConfigClass = config_dict.get(ENV, DevelopmentConfig)
