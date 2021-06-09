from codingbat.Warmup_2.front_times import front_times

def test_front_times():
    assert front_times("chocolate", 2) == "chocho"
        
def test2_front_times():
    assert front_times("Ab", 4) == "AbAbAbAb"

def test3_front_times():
    assert front_times("coast", 1) == "coa"
        
