from COURSE.MODULE5.libraries.csv import CsvFactory

def test_CsvFactory():
    data = CsvFactory().main()
    assert isinstance(data, (list) )
    assert len(data) > 0