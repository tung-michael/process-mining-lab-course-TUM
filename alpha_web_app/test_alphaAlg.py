from posixpath import join
from process_mining_alg.alphaAlg import Alpha_alg
from process_mining_alg.xes_importer import parseXes
import unittest
from file_path import TESTSET_DIRECTORY

class TestAlphaAlg(unittest.TestCase):
    
    def test_L1(self):
        log1 = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'L1.xes')))
        
        # L1-expected results
        L1_TL = {'a', 'c', 'b', 'd', 'e'}
        L1_TI = {'a'}
        L1_TO = {'d'}
        L1_XL = {(frozenset({'a'}),frozenset({'b'})),(frozenset({'a'}),frozenset({'c'})),(frozenset({'a'}),frozenset({'e'})),(frozenset({'b'}),frozenset({'d'})),(frozenset({'c'}),frozenset({'d'})),(frozenset({'e'}),frozenset({'d'})),(frozenset({'a'}),frozenset({'b','e'})),(frozenset({'a'}),frozenset({'c','e'})),(frozenset({'b','e'}),frozenset({'d'})),(frozenset({'c','e'}),frozenset({'d'}))}
        L1_YL = {(frozenset({'a'}), frozenset({'b', 'e'})), (frozenset({'a'}), frozenset({'c', 'e'})), (frozenset({'c', 'e'}), frozenset({'d'})), (frozenset({'b', 'e'}), frozenset({'d'}))}
        
        self.assertEqual(log1.events_set, L1_TL)
        self.assertEqual(log1.start_event, L1_TI)
        self.assertEqual(log1.end_event, L1_TO)
        self.assertEqual(log1.all_causal_pairs, L1_XL)
        self.assertEqual(log1.max_causal_pairs, L1_YL)
        
    def test_L2(self): # L2.xes
        log2 = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'L2.xes')))
        
        # L2-expected results
        L2_TL = {'a','b','c','d','e','f'}
        L2_TI = {'a'}
        L2_TO = {'d'}
        L2_XL = {(frozenset({'a'}), frozenset({'c'})), (frozenset({'a'}), frozenset({'b'})), (frozenset({'a', 'f'}), frozenset({'c'})), (frozenset({'f'}), frozenset({'c'})), (frozenset({'a', 'f'}), frozenset({'b'})), (frozenset({'f'}), frozenset({'b'})), (frozenset({'b'}), frozenset({'d', 'e'})), (frozenset({'b'}), frozenset({'d'})), (frozenset({'c'}), frozenset({'e'})), (frozenset({'e'}), frozenset({'f'})), (frozenset({'b'}), frozenset({'e'})), (frozenset({'c'}), frozenset({'d', 'e'})), (frozenset({'c'}), frozenset({'d'}))}
        L2_YL = {(frozenset({'a', 'f'}), frozenset({'c'})), (frozenset({'a', 'f'}), frozenset({'b'})), (frozenset({'c'}), frozenset({'d', 'e'})), (frozenset({'b'}), frozenset({'d', 'e'})), (frozenset({'e'}), frozenset({'f'}))}
        
        self.assertEqual(log2.events_set, L2_TL)
        self.assertEqual(log2.start_event, L2_TI)
        self.assertEqual(log2.end_event, L2_TO)
        self.assertEqual(log2.all_causal_pairs, L2_XL)
        self.assertEqual(log2.max_causal_pairs, L2_YL)
            
    def test_L3(self): # L3.xes
        log3 = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'L3.xes')))
        
        L3_TL = {'a','b','c','d','e','f','g'}
        L3_TI = {'a'}
        L3_TO = {'g'}

        L3_XL = {(frozenset({'a'}), frozenset({'b'})), (frozenset({'e'}), frozenset({'f'})), (frozenset({'f'}), frozenset({'b'})), (frozenset({'e'}), frozenset({'g'})), (frozenset({'a', 'f'}), frozenset({'b'})), (frozenset({'b'}), frozenset({'c'})), (frozenset({'b'}), frozenset({'d'})), (frozenset({'c'}), frozenset({'e'})), (frozenset({'d'}), frozenset({'e'})), (frozenset({'e'}), frozenset({'f', 'g'}))}

        L3_YL = {(frozenset({'a', 'f'}), frozenset({'b'})), (frozenset({'b'}), frozenset({'c'})), (frozenset({'b'}), frozenset({'d'})), (frozenset({'c'}), frozenset({'e'})),(frozenset({'d'}), frozenset({'e'})), (frozenset({'e'}), frozenset({'f', 'g'}))}

        self.assertEqual(log3.events_set, L3_TL)
        self.assertEqual(log3.start_event, L3_TI)
        self.assertEqual(log3.end_event, L3_TO)
        self.assertEqual(log3.all_causal_pairs, L3_XL)
        self.assertEqual(log3.max_causal_pairs, L3_YL)
        
    def test_L4(self): # L4.xes
        log4 = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'L4.xes')))
        L4_TL = {'a','b','c','d','e'}
        L4_TI = {'a','b'}
        L4_TO = {'d','e'}

        L4_XL = {(frozenset({'a'}), frozenset({'c'})), (frozenset({'c'}), frozenset({'d'})), (frozenset({'b'}), frozenset({'c'})), (frozenset({'c'}), frozenset({'e'})), (frozenset({'a', 'b'}), frozenset({'c'})),(frozenset({'c'}), frozenset({'d', 'e'})) }

        L4_YL = {(frozenset({'b', 'a'}), frozenset({'c'})), (frozenset({'c'}), frozenset({'e', 'd'}))}
        
        self.assertEqual(log4.events_set, L4_TL)
        self.assertEqual(log4.start_event, L4_TI)
        self.assertEqual(log4.end_event, L4_TO)
        self.assertEqual(log4.all_causal_pairs, L4_XL)
        self.assertEqual(log4.max_causal_pairs, L4_YL)
        
    def test_L5(self): # L5.xes
        log5 = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'L5.xes')))

        L5_TL = {'a','b','c','d','e','f'}
        L5_TI = {'a'}
        L5_TO = {'f'}

        L5_XL = {(frozenset({'a'}), frozenset({'e'})), (frozenset({'a'}), frozenset({'b'})), (frozenset({'d'}), frozenset({'b'})),(frozenset({'b'}), frozenset({'c'})), (frozenset({'b'}), frozenset({'f'})), (frozenset({'e'}), frozenset({'f'})), (frozenset({'c'}), frozenset({'d'})),(frozenset({'a', 'd'}), frozenset({'b'})), (frozenset({'b'}), frozenset({'c', 'f'}))}

        L5_YL = {(frozenset({'a'}), frozenset({'e'})), (frozenset({'a', 'd'}), frozenset({'b'})), (frozenset({'b'}), frozenset({'c', 'f'})), (frozenset({'e'}), frozenset({'f'})), (frozenset({'c'}), frozenset({'d'}))}
        
        self.assertEqual(log5.events_set, L5_TL)
        self.assertEqual(log5.start_event, L5_TI)
        self.assertEqual(log5.end_event, L5_TO)
        self.assertEqual(log5.all_causal_pairs, L5_XL)
        self.assertEqual(log5.max_causal_pairs, L5_YL)
        
    def test_L6(self): # L6.xes
        log6 = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'L6.xes')))
        L6_TL = {'a','b','c','d','e','f','g'}
        L6_TI = {'a','b'}
        L6_TO = {'g'}

        L6_XL = {(frozenset({'a'}), frozenset({'e'})), (frozenset({'a'}), frozenset({'c'})), (frozenset({'b'}), frozenset({'d'})), (frozenset({'b'}), frozenset({'f'})), (frozenset({'c'}), frozenset({'g'})), (frozenset({'d'}), frozenset({'g'})), (frozenset({'e'}), frozenset({'g'})), (frozenset({'f'}), frozenset({'g'})), (frozenset({'d', 'e'}), frozenset({'g'})), (frozenset({'c', 'd'}), frozenset({'g'})), (frozenset({'e', 'f'}), frozenset({'g'})), (frozenset({'c', 'f'}), frozenset({'g'}))}

        L6_YL = {(frozenset({'a'}), frozenset({'e'})), (frozenset({'a'}), frozenset({'c'})), (frozenset({'b'}), frozenset({'d'})), (frozenset({'b'}), frozenset({'f'})), (frozenset({'d', 'e'}), frozenset({'g'})), (frozenset({'c', 'd'}), frozenset({'g'})), (frozenset({'e', 'f'}), frozenset({'g'})), (frozenset({'c', 'f'}), frozenset({'g'}))}

        self.assertEqual(log6.events_set, L6_TL)
        self.assertEqual(log6.start_event, L6_TI)
        self.assertEqual(log6.end_event, L6_TO)
        self.assertEqual(log6.all_causal_pairs, L6_XL)
        self.assertEqual(log6.max_causal_pairs, L6_YL)
        
    def test_L7(self): # L7.xes
        log7 = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'L7.xes')))
        L7_TL = {'a','b','c'}
        L7_TI = {'a'}
        L7_TO = {'c'}
        L7_XL = {(frozenset({'a'}), frozenset({'c'}))}
        L7_YL = L7_XL

        self.assertEqual(log7.events_set, L7_TL)
        self.assertEqual(log7.start_event, L7_TI)
        self.assertEqual(log7.end_event, L7_TO)
        self.assertEqual(log7.all_causal_pairs, L7_XL)
        self.assertEqual(log7.max_causal_pairs, L7_YL)
        
    def test_re(self): # running-example.xes           
        log_re = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'running-example.xes')))
        
        RE_TL = {'register request', 'check ticket', 'examine casually', 'examine thoroughly', 'decide', 'pay compensation', 'reject request','reinitiate request'}
        RE_TI = {'register request'}
        RE_TO = {'pay compensation', 'reject request'}

        RE_XL = {(frozenset({'register request', 'reinitiate request'}),frozenset({'check ticket'})),
                (frozenset({'register request'}),frozenset({'check ticket'})),
                (frozenset({'reinitiate request'}),frozenset({'check ticket'})),
                (frozenset({'register request', 'reinitiate request'}),frozenset({'examine casually', 'examine thoroughly'})),
                (frozenset({'register request'}),frozenset({'examine casually'})),
                (frozenset({'register request'}),frozenset({'examine thoroughly'})),
                (frozenset({'reinitiate request'}),frozenset({'examine casually'})),
                (frozenset({'reinitiate request'}),frozenset({'examine thoroughly'})),
                (frozenset({'register request', 'reinitiate request'}),frozenset({'examine casually'})),
                (frozenset({'register request', 'reinitiate request'}),frozenset({'examine thoroughly'})),
                (frozenset({'register request'}),frozenset({'examine casually', 'examine thoroughly'})),
                (frozenset({'reinitiate request'}),frozenset({'examine casually', 'examine thoroughly'})),
                (frozenset({'examine casually'}),frozenset({'decide'})),
                (frozenset({'examine thoroughly'}),frozenset({'decide'})),
                (frozenset({'examine casually', 'examine thoroughly'}),frozenset({'decide'})),
                (frozenset({'check ticket'}),frozenset({'decide'})),
                (frozenset({'decide'}),frozenset({'pay compensation', 'reject request', 'reinitiate request'})),
                (frozenset({'decide'}),frozenset({'pay compensation', 'reinitiate request'})),
                (frozenset({'decide'}),frozenset({'reject request', 'reinitiate request'})),
                (frozenset({'decide'}),frozenset({'pay compensation', 'reject request'})),
                (frozenset({'decide'}),frozenset({'pay compensation'})),
                (frozenset({'decide'}),frozenset({'reject request'})),
                (frozenset({'decide'}),frozenset({'reinitiate request'}))}


        RE_YL = {(frozenset({'register request', 'reinitiate request'}),frozenset({'check ticket'})),
                (frozenset({'register request', 'reinitiate request'}),frozenset({'examine casually', 'examine thoroughly'})),
                (frozenset({'examine casually', 'examine thoroughly'}),frozenset({'decide'})),
                (frozenset({'check ticket'}),frozenset({'decide'})),
                (frozenset({'decide'}),frozenset({'pay compensation', 'reject request', 'reinitiate request'}))
                }
        
        self.assertEqual(log_re.events_set, RE_TL)
        self.assertEqual(log_re.start_event, RE_TI)
        self.assertEqual(log_re.end_event, RE_TO)
        self.assertEqual(log_re.all_causal_pairs, RE_XL)
        self.assertEqual(log_re.max_causal_pairs, RE_YL)
        
    def test_fl(self): # flyerinstances.xes      
        log_flyer = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'flyerinstances.xes')))
        FL_TL = {'receive flyer order', 'design flyer', 'send draft to customer', 'print flyer', 'deliver flyer'}
        FL_TI = {'receive flyer order'}
        FL_TO = {'deliver flyer'}

        FL_XL = {(frozenset({'receive flyer order'}), frozenset({'design flyer'})), (frozenset({'send draft to customer'}), frozenset({'print flyer'})), (frozenset({'print flyer'}), frozenset({'deliver flyer'}))}

        FL_YL = FL_XL
        self.assertEqual(log_flyer.events_set, FL_TL)
        self.assertEqual(log_flyer.start_event, FL_TI)
        self.assertEqual(log_flyer.end_event, FL_TO)
        self.assertEqual(log_flyer.all_causal_pairs, FL_XL)
        self.assertEqual(log_flyer.max_causal_pairs, FL_YL)    
    
    def test_bill(self): # billinstances.xes   
        log_bill = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'billinstances.xes')))
        
        BI_TL = {'write bill', 'print bill', 'deliver bill'}
        BI_TI = {'write bill'}
        BI_TO = {'deliver bill'}
        BI_XL = {(frozenset({'write bill'}), frozenset({'print bill'})), (frozenset({'print bill'}), frozenset({'deliver bill'}))}
        BI_YL = BI_XL

        self.assertEqual(log_bill.events_set, BI_TL)
        self.assertEqual(log_bill.start_event, BI_TI)
        self.assertEqual(log_bill.end_event, BI_TO)
        self.assertEqual(log_bill.all_causal_pairs, BI_XL)
        self.assertEqual(log_bill.max_causal_pairs, BI_YL)    
        
    def test_poster(self): # posterinstances.xes       
        log_poster = Alpha_alg(parseXes(join(TESTSET_DIRECTORY,'posterinstances.xes')))
        
        PO_TL = {'receive order and photo', 'design photo poster', 'print poster', 'deliver poster'}
        PO_TI = {'receive order and photo'}
        PO_TO = {'deliver poster'}
        PO_XL = {(frozenset({'receive order and photo'}), frozenset({'design photo poster'})), (frozenset({'design photo poster'}), frozenset({'print poster'})), (frozenset({'print poster'}), frozenset({'deliver poster'}))}
        PO_YL = PO_XL

        self.assertEqual(log_poster.events_set, PO_TL)
        self.assertEqual(log_poster.start_event, PO_TI)
        self.assertEqual(log_poster.end_event, PO_TO)
        self.assertEqual(log_poster.all_causal_pairs, PO_XL)
        self.assertEqual(log_poster.max_causal_pairs, PO_YL)    
        
            
if __name__ == "__main__":
    unittest.main()