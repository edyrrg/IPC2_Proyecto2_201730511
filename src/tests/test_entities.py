from src.models.entities.mock_up import MockUp


def test_entities():
    mock_up = MockUp(name="Modelo1", rows=5, columns=5)
    print(mock_up.__str__())


if __name__ == '__main__':
    test_entities()
