'''
Author: mukangt
Date: 2020-12-14 14:39:47
LastEditors: mukangt
LastEditTime: 2020-12-15 14:31:35
Description: 
'''

import bisect
import hashlib


class HashRing():
    def __init__(self, nodes, replicas=3):
        self.replicas = replicas
        self.ring = dict()
        self._sorted_keys = list()

        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        '''
        description: add a node to the hash ring (including a number of replicas)
        param {node} to be added
        return {*}
        '''
        for i in range(self.replicas):
            virtual_node = '{}#{}'.format(node, i)
            key = self._gen_key(virtual_node)
            self.ring[key] = node
            self._sorted_keys.append(key)

        self._sorted_keys.sort()

    def remove_node(self, node):
        '''
        description: remove a node from the hash ring and its replicas
        param {node} to be removed
        return {*}
        '''
        for i in range(self.replicas):
            virtual_node = '{}#{}'.format(node, i)
            key = self._gen_key(virtual_node)
            del self.ring[key]
            self._sorted_keys.remove(key)

    def get_node(self, string_key):
        '''
        description: return corresponding node in hash ring by the string key
        param {sting_key} a string key
        return {*}
        '''
        if not self.ring:
            return None

        pos = self._get_node_pos(string_key)
        key = self._sorted_keys[pos]
        return self.ring[key]

    def _get_node_pos(self, string_key):
        '''
        description: return corresponding node key  by the string key
        param {*}
        return {*}
        '''
        key = self._gen_key(string_key)
        pos = bisect.bisect(self._sorted_keys, key)

        if pos == len(self._sorted_keys):
            pos = 0

        return pos

    def _gen_key(self, string_key):
        '''
        description: 
        param {string_key}string key for hash
        return {hex_value}long hex value
        '''
        m = hashlib.md5()
        m.update(string_key.encode(encoding='utf-8'))
        return m.hexdigest()


if __name__ == "__main__":
    nodes = ['172.20.111.116:41967', '172.20.111.21:41967']

    hash_ring = HashRing(nodes)
    import time
    node = hash_ring.get_node(str(time.time()))
    print(node)
