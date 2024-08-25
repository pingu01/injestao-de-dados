from unittest.mock import patch, MagicMock
import pytest
from data_pipeline.minio_client import upload_file

def test_upload_file():
    bucket_name = "test-bucket"
    file_path = "/path/to/testfile.txt"
    file_name = "testfile.txt"

    with patch("data_pipeline.minio_client.minio_client") as mock_minio_client:
        mock_minio_client.fput_object = MagicMock()

        upload_file(bucket_name, file_path)

        mock_minio_client.fput_object.assert_called_once_with(bucket_name, file_name, file_path)

def test_upload_file_nonexistent():
    bucket_name = "test-bucket"
    file_path = "/path/to/nonexistentfile.txt"

    with patch("data_pipeline.minio_client.minio_client") as mock_minio_client:
        mock_minio_client.fput_object = MagicMock(side_effect=FileNotFoundError)

        with pytest.raises(FileNotFoundError):
            upload_file(bucket_name, file_path)