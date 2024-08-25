import pytest
import pandas as pd
import pyarrow.parquet as pq
import os

from data_pipeline.data_processing import process_data

def test_process_data():
    # Sample data
    data = {'col1': 'value1', 'col2': 'value2'}
    
    # Call the function
    filename = process_data(data)
    
    # Check if the filename is a string and ends with .parquet
    assert isinstance(filename, str)
    assert filename.endswith('.parquet')
    
    # Check if the file exists
    assert os.path.exists(filename)
    
    # Read the Parquet file
    table = pq.read_table(filename)
    df = table.to_pandas()
    
    # Check if the content matches the sample data
    assert df.to_dict(orient='records')[0] == data
    
    # Clean up
    os.remove(filename)