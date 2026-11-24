from app import lesson

def test_offline_lesson(monkeypatch):
    monkeypatch.delenv('OPENAI_API_KEY',raising=False)
    result=lesson('Addition within 10','1')
    assert result['mode']=='Offline template'
    assert 'Addition within 10' in result['lesson'] and 'Exit ticket' in result['lesson']
