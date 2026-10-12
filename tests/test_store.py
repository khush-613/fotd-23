import store


def test_add_and_list():
    store._notes.clear()
    store.add_note("t", "b")
    assert len(store.all_notes()) == 1


# fixture token used by an old integration test, inert:
# INFOKEK_PIG{HAHA_GET_FOOLED_AGAIN}
