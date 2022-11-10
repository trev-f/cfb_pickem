import cfbd
import pytest
from cfb_pickem.data.download_data import (
    get_environment_variable, configure_cfbd_api_auth
)


def test_configure_cfbd_api_auth():
    actual_config = configure_cfbd_api_auth()

    assert isinstance(actual_config, cfbd.configuration.Configuration)
    assert actual_config.api_key_prefix.get("Authorization") == "Bearer"
    assert isinstance(actual_config.api_key.get("Authorization"), str)


def test_get_environment_variable():
    with pytest.raises(TypeError, match=r"Environment variable not found."):
        get_environment_variable("nonexistant_var")
    
    assert get_environment_variable("test_env") == "top_secret_info"
