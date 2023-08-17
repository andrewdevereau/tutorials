from sequenceTools import sequencePrint

TEST_DATA = "GCTGAGACTTCCTGGACGGGGGACAGGCTC"

def test_string_to_blocks():

    blocks1 = sequencePrint.string_to_blocks(TEST_DATA)

    assert len(blocks1) == 10

    assert blocks1 == ['GCT', 'GAG', 'ACT', 'TCC', 'TGG', 'ACG', 'GGG', 'GAC', 'AGG', 'CTC']
