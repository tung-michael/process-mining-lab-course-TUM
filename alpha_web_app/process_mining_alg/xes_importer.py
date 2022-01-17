import re

class EventLog:
    """This class models an EventLog with the properties corresponding to those of a standard .xes file.    
    """
    
    def __init__(self):
        self.extensions =[] # list of extensions as type string
        self.gl_att = {'trace':[], 'event':[]} # global attributes of trace and event
        self.traces = [] # list of traces: list[{*'trace_attribute': 'value', 'events':list()}]
                         # a trace is a dictionary containing trace attributes and events
        self.classifier = {} # dictionary of event classifier 'name' : 'keys'

def _extract(line,start,end): 
    # extract the string between 'start' and 'end' in the 'line'
    try:
        return re.search(start+"(.+?)"+end,line).group(1)
    except AttributeError:
        return "None"

def _name_tag(line): # extract name tag of the 'line'
    line=line.strip()
    if "</" in line or ("/" not in line and "=" not in line):
        return _extract(line,'<','>')
    else:
        return _extract(line,'<',' ')

def _value_of(line, keyword): 
    # return the value assigned to keyword in the line
    # e.g: string="something" ---> return 'something'
    line=line.strip()
    return _extract(line,keyword+'="','"')

def parseXes(filepath):
    """Retrieves the parsed log.

        :return: the parsed log.
        :rtype: `EventLog`
    """
    file = open(filepath, "r")
    log = EventLog()
    
    for line in file:
        if _name_tag(line) == "extension":
            log.extensions.append(re.search("<extension (.+?)/>",line).group(1))
        elif _name_tag(line) == "classifier": 
            name = _value_of(line,'name')
            keys = _value_of(line,'keys')
            if ' ' in keys:
                keys = keys.split()
            log.classifier[name] = keys
        elif _name_tag(line) == "global":
            if "trace" in line:
                line = file.readline()
                while "/global" not in line:
                    log.gl_att['trace'].append(_value_of(line,'key'))
                    line = file.readline()
            elif "event" in line:
                line = file.readline()
                while "/global" not in line:
                    log.gl_att['event'].append(_value_of(line,'key'))
                    line = file.readline()
        elif _name_tag(line) == "trace":
            log.traces.append({}) # append new empty trace
            events = []
            line = file.readline()
            while "/trace" not in line: # loop through every line until the end of  this trace
                while _name_tag(line) in ["string", "date", "float", "int", "boolean"]: # info lines of the trace
                    log.traces[-1][_value_of(line,'key')] = _value_of(line,'value')
                    line = file.readline()

                if _name_tag(line) == "event":
                    line = file.readline()
                    current_event = {}
                    while "/event" not in line:
                        current_event[_value_of(line,'key')] = _value_of(line,'value')
                        line = file.readline()
                    events.append(current_event)
                line = file.readline()
            log.traces[-1]['events'] = events
    file.close()    
    return log

def simplify_log(log: EventLog): 
    """Simplifies the parsed EventLog for easier processing with alpha miner.

        :return: the simplified log.
        :rtype: list[list[str]]
    """
    compact_log = []   
    for trace in log.traces:
        events_list = []
        for event in trace['events']:
            # only sampling events with 'lifecycle:transition' = 'complete' or events without this attribute
            if 'lifecycle:transition' not in event or event['lifecycle:transition'] == 'complete':
                events_list.append(event['concept:name'])
        compact_log.append(events_list)
    return compact_log
