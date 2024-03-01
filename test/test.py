from myPackage import myModule

def test_top_n() :
    """
    make sure top_n work correctly
    """

    assert  myModule.top_n([18,54,18,49,60],3) == [60,54,49] ,  "incorrect" 
    assert  myModule.top_n([5,95,60,58,39],4) == [95,60,58,39] ,  "incorrect" 
    assert  myModule.top_n([54,94,49,39,93],5) == [94,93,54,49,39] ,  "incorrect" 
