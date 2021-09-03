from storage import get_rankings

def test_can_get_rankings():
  rankings = get_rankings()
  assert len(rankings) > 0