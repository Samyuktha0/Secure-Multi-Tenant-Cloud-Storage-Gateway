from gateway.storage import upload_file, download_file

def test_storage():
    test_data = b"sample data"
    upload_file("test.txt", test_data)
    result = download_file("test.txt")
    assert result == test_data
