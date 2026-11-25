import argparse
import os
from pathlib import Path

import yaml


SCHEMAS = {
    "import": "rel-hm",
    "export": "rel-hm_synthetic",
}


def create_snowflake_configs(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    for config_type, schema_name in SCHEMAS.items():
        config = {
            "connection": {
                "database_name": "SNOWFLAKE_CONNECTOR_TEST",
                "schema_name": schema_name,
            },
            "auth": {
                "username": os.environ["SNOWFLAKE_USERNAME"],
                "password": "",
            },
            "runtime": {
                "connection_timeout": 300,
            },
            "options.SnowflakeConnector": {
                "account_identifier": os.environ["SNOWFLAKE_ACCOUNT_IDENTIFIER"],
                "warehouse": os.environ["SNOWFLAKE_WAREHOUSE"],
                "role": os.environ["SNOWFLAKE_ROLE"],
                "private_key_file": "~/.snowflake/keys/rsa_key.p8",
                "private_key_password": os.environ["SNOWFLAKE_RSA_PASSWORD"],
            },
        }

        config_path = output_dir / f"snowflake_{config_type}_config.yaml"

        with config_path.open("w") as file:
            yaml.safe_dump(config, file, sort_keys=False)

        print(f"Created {config_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Snowflake import/export configurations"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory where YAML files will be created",
    )

    args = parser.parse_args()
    create_snowflake_configs(args.output_dir)
