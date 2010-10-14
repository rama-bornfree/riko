"""Unit tests using basic pipeline modules"""

import unittest

from pipe2py import Context
import pipe2py.compile

import os.path
import fileinput
try:
    import json
except ImportError:
    import simplejson as json
    
    
class TestBasics(unittest.TestCase):
    """Test a few sample pipelines
    
       Note: asserting post-conditions for these is almost impossible because
             many use live sources.
             
             See createtest.py for an attempt at creating a stable test-suite.
    """
    
    def setUp(self):
        """Compile common subpipe"""
        self.context = Context(test=True)
        name = "pipe_2de0e4517ed76082dcddf66f7b218057"
        pipe_def = self._get_pipe_def("%s.json" % name)
        fp = open("%s.py" % name, "w")   #todo confirm file overwrite
        print >>fp, pipe2py.compile.parse_and_write_pipe(self.context, pipe_def, pipe_name=name)
    
    def tearDown(self):
        name = "pipe_2de0e4517ed76082dcddf66f7b218057"
        os.remove("%s.py" % name)
    
    def _get_pipe_def(self, filename):
        pjson = []
        for line in fileinput.input(filename):
            pjson.append(line)    
        pjson = "".join(pjson)
        pipe_def = json.loads(pjson)
        
        return pipe_def
        

    def test_feed(self):
        """Loads a simple test pipeline and compiles and executes it to check the results
       
           TODO: have these tests iterate over a number of test pipelines
        """
        pipe_def = self._get_pipe_def("testpipe1.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        count = 0
        for i in p:
            count += 1
            self.assertTrue("the" in i.get('description'))
            
        self.assertEqual(count, 4)

    def test_simplest(self):
        """Loads the RTW simple test pipeline and compiles and executes it to check the results
        """
        pipe_def = self._get_pipe_def("pipe_2de0e4517ed76082dcddf66f7b218057.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        count = 0
        for i in p:
            count += 1
            
        self.assertTrue(count > 0)

    #Note: this test will be skipped for now
    # - it requires a TermExtractor module which isn't top of the list
    #def test_simpletagger(self):
        #"""Loads the RTW simple tagger pipeline and compiles and executes it to check the results
        #"""Note: uses a subpipe pipe_2de0e4517ed76082dcddf66f7b218057 (assumes its been compiled to a .py file - see test setUp)
        #"""
        #pipe_def = self._get_pipe_def("pipe_93abb8500bd41d56a37e8885094c8d10.json")
        #p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        ##todo: check the data!
        #count = 0
        #for i in p:
            #count += 1
            
        #self.assertTrue(count > 0)
        
    def test_filtered_multiple_sources(self):
        """Loads the filter multiple sources pipeline and compiles and executes it to check the results
           Note: uses a subpipe pipe_2de0e4517ed76082dcddf66f7b218057 (assumes its been compiled to a .py file - see test setUp)
        """
        pipe_def = self._get_pipe_def("pipe_c1cfa58f96243cea6ff50a12fc50c984.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        #todo: check the data!
        count = 0
        for i in p:
            count += 1
            
        self.assertTrue(count > 0)
        
    def test_urlbuilder(self):
        """Loads the RTW URL Builder test pipeline and compiles and executes it to check the results
        """
        pipe_def = self._get_pipe_def("pipe_e519dd393f943315f7e4128d19db2eac.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        #todo: check the data!
        count = 0
        for i in p:
            count += 1
            
        #self.assertTrue(count > 0)
        
    def test_twitter_caption_search(self):
        """Loads the Twitter Caption Search pipeline and compiles and executes it to check the results
        """
        pipe_def = self._get_pipe_def("pipe_eb3e27f8f1841835fdfd279cd96ff9d8.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        #todo: check the data!
        count = 0
        for i in p:
            count += 1
            
        self.assertTrue(count > 0)

    def test_loop_example(self):
        """Loads the loop example pipeline and compiles and executes it to check the results
        """
        pipe_def = self._get_pipe_def("pipe_dAI_R_FS3BG6fTKsAsqenA.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        #todo: check the data! e.g. pubdate etc.
        count = 0
        for i in p:
            count += 1
            
        self.assertTrue(count == 1)
        self.assertEqual(i['title'], " THIS TSUNAMI ADVISORY IS FOR ALASKA/ BRITISH COLUMBIA/ WASHINGTON/ OREGON\n            AND CALIFORNIA ONLY\n             (Severe)")
        
    def test_european_performance_cars(self):
        """Loads a pipeline containing a sort
        """
        pipe_def = self._get_pipe_def("pipe_8NMkiTW32xGvMbDKruymrA.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        #todo: check the data! e.g. pubdate etc.
        count = 0
        for i in p:
            count += 1
            
        self.assertTrue(count > 0)
    
    def test_twitter(self):
        """Loads a pipeline containing a loop, complex regex etc. for twitter
        """
        pipe_def = self._get_pipe_def("pipe_ac45e9eb9b0174a4e53f23c4c9903c3f.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        #todo: check the data! e.g. pubdate etc.
        count = 0
        for i in p:
            count += 1
            
    def test_reverse_truncate(self):
        """Loads a pipeline containing a reverse and truncate
        """
        pipe_def = self._get_pipe_def("pipe_58a53262da5a095fe7a0d6d905cc4db6.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        count = 0
        prev_title = None
        for i in p:
            self.assertTrue(not prev_title or i['title'] < prev_title)
            prev_title = i['title']
            count += 1
            
        self.assertTrue(count == 3)
        
    def test_count_truncate(self):
        """Loads a pipeline containing a count and truncate
        """
        pipe_def = self._get_pipe_def("pipe_58a53262da5a095fe7a0d6d905cc4db6.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        #todo: check the data! e.g. pubdate etc.
        count = 0
        for i in p:
            count += 1
            
        self.assertTrue(count == 3)

    def test_yql(self):
        """Loads a pipeline containing a yql query
        """
        pipe_def = self._get_pipe_def("pipe_80fb3dfc08abfa7e27befe9306fc3ded.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        count = 0
        for i in p:
            count += 1
            self.assertTrue(i['title'] == i['a']['content'])
            
        self.assertTrue(count > 0)

    def test_itembuilder(self):
        """Loads a pipeline containing an itembuilder
        """
        pipe_def = self._get_pipe_def("pipe_b96287458de001ad62a637095df33ad5.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        count = 0
        match = 0
        for i in p:
            count += 1
            if i == {u'attrpath': {u'attr2': u'VAL2'}, u'ATTR1': u'VAL1'}:
                match +=1
            if i == {u'longpath': {u'attrpath': {u'attr3': u'val3'}}, u'attrpath': {u'attr2': u'val2', u'attr3': u'extVal'}, u'attr1': u'val1'}:
                match +=1
            
        self.assertTrue(count == 2)
        self.assertTrue(match == 2)

    def test_rssitembuilder(self):
        """Loads a pipeline containing an rssitembuilder
        """
        pipe_def = self._get_pipe_def("pipe_1166de33b0ea6936d96808717355beaa.json")
        p = pipe2py.compile.parse_and_build_pipe(self.context, pipe_def)
        
        count = 0
        match = 0
        for i in p:
            count += 1
            if i == {'media:thumbnail': {'url': u'http://example.com/a.jpg'}, u'link': u'http://example.com/test.php?this=that', u'description': u'b', u'y:title': u'a', u'title': u'a'}:
                match +=1
            if i == {u'newtitle': u'NEWTITLE', u'loop:itembuilder': {u'description': {u'content': u'DESCRIPTION'}, u'title': u'NEWTITLE'}, u'title': u'TITLE1'}:
                match +=1
            if i == {u'newtitle': u'NEWTITLE', u'loop:itembuilder': {u'description': {u'content': u'DESCRIPTION'}, u'title': u'NEWTITLE'}, u'title': u'TITLE2'}:
                match +=1
            
        self.assertTrue(count == 3)
        self.assertTrue(match == 3)
        
    #todo test malformed pipeline syntax too
    
    #todo test pipe compilation too, i.e. compare output against an expected .py file

if __name__ == '__main__':
    unittest.main()
