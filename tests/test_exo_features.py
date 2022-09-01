from COURSE.MODULE5.exo import concat_data, add_random_currencies, add_random_countries,CsvFactory, JsonFactory, HtmlFactory


def test_concat_data():
    j_data, h_data, c_data = JsonFactory.main(),HtmlFactory.main(),CsvFactory.main()
    all_data = concat_data(list_of_data=[JsonFactory.main(),HtmlFactory.main(),CsvFactory.main() ])
    
    assert len(all_data) == len(j_data)+ len(h_data)+len(c_data)

# VAR for incoming tests
DATA = JsonFactory.main() # concat_data(list_of_data=[JsonFactory.main(),HtmlFactory.main(),CsvFactory.main() ])


def test_add_random_currencies():
    new_data = add_random_currencies(data=DATA)
    new_keys = list(new_data[0].keys())

    assert "currency" in new_keys
    assert "conv_to_xof" in new_keys
    
def test_add_random_countries():
    new_data = add_random_countries(data=DATA)
    new_keys = list(new_data[0].keys())

    assert "country" in new_keys
    assert "flag" in new_keys
    