from COURSE.MODULE5.libraries.json import JsonFactory

def test_JsonFactory():
    data = JsonFactory().main()
    assert isinstance(data, (list) )
    assert len(data) > 0