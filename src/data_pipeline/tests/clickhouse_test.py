
import pytest
from unittest.mock import patch, MagicMock
import tempfile
import os
from data_pipeline.clickhouse_client import execute_sql_script

@patch('data_pipeline.clickhouse_client.get_client')
def test_execute_sql_script(mock_get_client):
    # Create a mock client
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    # Create a temporary SQL script file
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.sql') as temp_sql_file:
        temp_sql_file.write("SELECT * FROM test_table;")
        temp_sql_file_path = temp_sql_file.name

    try:
        # Call the function to test
        execute_sql_script(temp_sql_file_path)

        # Assert that the command method was called with the correct SQL script
        mock_client.command.assert_called_once_with("SELECT * FROM test_table;")
    finally:
        # Clean up the temporary file
        os.remove(temp_sql_file_path)