from processranking.storage import get_rankings

def test_can_get_rankings():
  # just check that it runs without failure
  rankings = get_rankings()
  assert len(rankings) >= 0