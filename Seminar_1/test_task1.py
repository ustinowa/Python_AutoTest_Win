from func_for_tes import check_text


def test_step1(incorrect_word, correct_word):
    assert correct_word in check_text(incorrect_word), "Test1 FAIL"