from os.path import join
from pathlib import Path

PROJECT_DIRECTORY = Path(__file__).parents[1] # Process Mining Code
WEBAPP_DIRECTORY = join(PROJECT_DIRECTORY, 'alpha_web_app') # Process Mining Code/alpha_web_app
ALG_DIRECTORY = join(WEBAPP_DIRECTORY, 'process_mining_alg') # Process Mining Code/alpha_web_app/process_mining_alg
TESTSET_DIRECTORY = join(ALG_DIRECTORY, 'test_set') # Process Mining Code/alpha_web_app/process_mining_alg/test_set


