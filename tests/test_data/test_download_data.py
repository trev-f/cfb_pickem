import pytest
from cfb_pickem.data.download_data import (
    get_environment_variable
)


def test_get_environment_variable():
    with pytest.raises(TypeError, match=r"Environment variable not found."):
        get_environment_variable("nonexistant_var")
    
    assert get_environment_variable("test_env") == "top_secret_info"
