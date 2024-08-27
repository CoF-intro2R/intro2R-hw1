# autograding

import os
import re
import pytest

def test_dir_struc():
  assert os.path.isdir("R")
  assert os.path.isdir("Figures")
  assert os.path.isfile("R/hw1.R")
  assert os.path.isfile("Figures/sample_hist.png")

def uses_rel_path():
  if os.path.isfile("R/hw1.R"):
    
    with open("R/hw1.R", 'r') as script:
      content = script.read()
      
    # search for the specific line
    line = re.search(r'filename\s*=\s*["\'](.+?)["\']', content).group(0)
    
    # check if either here or relative paths are used
    match1 = re.search(r'filename\s*=\s*["\']Figures', line)
    match2 = re.search(r'filename\s*=\s*here\:\:here', line)
    
    res = bool(match1) | bool(match2)
    
    assert res == True
  
