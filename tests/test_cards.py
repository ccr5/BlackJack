from classes.cards import Cards as c


class TestCards:

    def test_show_card(self):
        result = c.show_card([c.matrix[0]])
        assert result == [["- - - -", "|     |",
                           f"|  A  |", "|     |", "- - - -"]]
