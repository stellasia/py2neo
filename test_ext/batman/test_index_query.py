#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2011-2016, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from py2neo import Node
from .util import IndexTestCase


class IndexQueryTestCase(IndexTestCase):
    
    def test_can_query_node_index(self):
        try:
            self.index_manager.delete_index(Node, "people")
        except LookupError:
            pass
        people = self.index_manager.get_or_create_index(Node, "people")
        people.create("name", "Alice", {"name": "Alice"})
        people.create("name", "Bob", {"name": "Bob"})
        c = people.create("name", "Carol", {"name": "Carol"})
        d = people.create("name", "Dave", {"name": "Dave"})
        people.create("name", "Eve", {"name": "Eve"})
        f = people.create("name", "Frank", {"name": "Frank"})
        for person in people.query("name:*a*"):
            assert person in (c, d, f)
        
    def test_can_query_node_index_with_score_by_index(self):
        try:
            self.index_manager.delete_index(Node, "people")
        except LookupError:
            pass
        people = self.index_manager.get_or_create_index(Node, "people")
        people.create("name", "Alice", {"name": "Alice"})
        people.create("name", "Bob", {"name": "Bob"})
        c = people.create("name", "Carol", {"name": "Carol"})
        d = people.create("name", "Dave", {"name": "Dave"})
        people.create("name", "Eve", {"name": "Eve"})
        f = people.create("name", "Frank", {"name": "Frank"})
        for person, score in people.query_by_index("name:*a*"):
            assert person in (c, d, f)
            assert isinstance(score, float)
        
    def test_can_query_node_index_with_score_by_relevance(self):
        try:
            self.index_manager.delete_index(Node, "people")
        except LookupError:
            pass
        people = self.index_manager.get_or_create_index(Node, "people")
        people.create("name", "Alice", {"name": "Alice"})
        people.create("name", "Bob", {"name": "Bob"})
        c = people.create("name", "Carol", {"name": "Carol"})
        d = people.create("name", "Dave", {"name": "Dave"})
        people.create("name", "Eve", {"name": "Eve"})
        f = people.create("name", "Frank", {"name": "Frank"})
        for person, score in people.query_by_relevance("name:*a*"):
            assert person in (c, d, f)
            assert isinstance(score, float)
        
    def test_can_query_node_index_with_score_by_score(self):
        try:
            self.index_manager.delete_index(Node, "people")
        except LookupError:
            pass
        people = self.index_manager.get_or_create_index(Node, "people")
        people.create("name", "Alice", {"name": "Alice"})
        people.create("name", "Bob", {"name": "Bob"})
        c = people.create("name", "Carol", {"name": "Carol"})
        d = people.create("name", "Dave", {"name": "Dave"})
        people.create("name", "Eve", {"name": "Eve"})
        f = people.create("name", "Frank", {"name": "Frank"})
        for person, score in people.query_by_score("name:*a*"):
            assert person in (c, d, f)
            assert isinstance(score, float)
