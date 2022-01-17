"""For running process mining algorithms on local machine."""
from file_path import join, TESTSET_DIRECTORY, WEBAPP_DIRECTORY
from process_mining_alg.alphaAlg import Alpha_alg
from process_mining_alg.xes_importer import parseXes

def executeAlpha(filepath):
    return Alpha_alg(parseXes(filepath))

def executeHeuristic(filepath):
    pass

if __name__ == "__main__":

    alpha =  executeAlpha(join(TESTSET_DIRECTORY,"L2.xes"))
    ptn = alpha.generate_petri_net()
    ptn.render(join(WEBAPP_DIRECTORY, 'output'), view = True)
    print (ptn.source)