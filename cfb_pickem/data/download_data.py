import click
from dotenv import load_dotenv
import logging
import os


logger = logging.getLogger(__name__)

def main():
    """
    Main logic for the subcommand download-data.
    This subcommand downloads data from an external source to `data/external`.
    """
    logger.info("Start the main function for downloading external data")

    click.echo("Download external data!")

    logger.info("End of the main function for downloading external data")


def get_cfbd_api_key() -> str:
    """Get the API key for CollegeFootballData.com

    :return: API key for CollegeFootballData.com
    :rtype: str
    """
    try:
        cfbd_api_key = get_environment_variable("cfbd_api_key")
    except TypeError as e:
        logger.exception(f"{e}: Environment variable 'cfbd_api_key' does not exist.")
    else:
        return cfbd_api_key


def get_environment_variable(env_var: str) -> str:
    """Return the value associated with an environment variable

    :param env_var: The environment variable
    :type env_var: str
    :raises TypeError: Environment variable is not fetched
    :return: The value associated with the environment variable
    :rtype: str
    """
    load_dotenv()
    value = os.getenv(env_var)
    if value is None:
        raise TypeError("Environment variable not found.")
    
    return value


if __name__ == "__main__":
    main()
