from COURSE.MODULE5.libraries.html import HtmlFactory
from typing import get_type_hints,  List, Dict

def test_HtmlFactory():
    data = HtmlFactory().main()
    assert isinstance(data, (list) )
    assert len(data) > 0