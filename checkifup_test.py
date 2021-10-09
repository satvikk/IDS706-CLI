import checkifup
import subprocess
import os

def test_url():
    r = subprocess.run(['checkifup', 'url', 'http://google.com'], stdout=subprocess.PIPE)
    assert r.stdout == b'Is up\n'
    pass

def test_concept():
    r = subprocess.run(['checkifup', 'concept', 'sky'], stdout=subprocess.PIPE)
    assert r.stdout == b'Yes!\n'
