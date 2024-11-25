from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings (BaseSettings):
    
    
    database_username:str
    database_password:str
    database_host:str 
    # database_port:int
    database_name:str
    SECRET_KEY:str
    ALOGRITHM:str
    ACCESS_EXPIRSE_TIME:int

    model_config= SettingsConfigDict(env_file=".env")


settings=Settings()