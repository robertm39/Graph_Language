# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:00:12 2020

@author: rober
"""

from enum import Enum

class Type(Enum):
    INT = 'INT'
    STR = 'STR'
    BOOL = 'BOOL'

class Null(Enum):
    NULL = 'NULL'

class Node:
    def __init__(self, node_func, value=None, input_nodes=None, is_input=False, is_output=False):
        self.node_func = node_func
        self.input_nodes = input_nodes[:] if input_nodes else []
        self.is_input = False
        self.is_output = False
        self.value = value
        self.has_value = self.value != None
    
    def get_value(self, force_eval=False):
        if self.has_value:
            return self.value
        
        #If every input node has its value
        if max([node.has_value for node in self.input_nodes]):
            values = [node.get_value() for node in self.input_nodes]
            self.value = self.node_func(*values)
            if self.value != None:
                self.has_value = True
            return self.value
        
        if force_eval:
            values = [node.get_value(force_eval=True) for node in self.input_nodes] 
            self.value = self.node_func(*values)
            if self.value != None:
                self.has_value = True
            return self.value
        
        return None

class NodeFunc:
    def __init__(self, func, symbol, in_types, out_types):
        self.func = func
        self.symbol = symbol[:]
        self.in_types = in_types[:]
        self.out_types = out_types[:]